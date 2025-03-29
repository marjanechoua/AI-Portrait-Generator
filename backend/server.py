from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from PIL import Image
import torch
import numpy as np
from diffusers import StableDiffusionXLImg2ImgPipeline

# Flask App initialisieren
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Konfigurationsparameter
UPLOAD_FOLDER = 'static/uploads'
GENERATED_FOLDER = 'static/generated'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Für SDXL sind 1024x1024 oft ein guter Startpunkt (sofern genügend VRAM vorhanden ist)
MAX_SIZE = (1024, 1024)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Max. 10 MB

# Sicherstellen, dass die Ordner existieren
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

# Stable Diffusion XL Modell laden (Base-Modell)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device)

def allowed_file(filename):
    """Prüft, ob die Datei ein zulässiges Bildformat hat."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_face_mask(image):
    """
    Erstellt eine einfache Gesichtsmaske.
    (Beispielhaft auf einen manuellen Bereich im Bild beschränkt.)
    """
    width, height = image.size
    mask = np.zeros((height, width), dtype=np.uint8)

    # Manueller Bereich für das Gesicht
    face_box = (width // 4, height // 5, width * 3 // 4, height * 3 // 4)
    mask[face_box[1]:face_box[3], face_box[0]:face_box[2]] = 255

    return Image.fromarray(mask)

@app.route('/')
def health_check():
    """Überprüft, ob die API läuft."""
    return jsonify({"message": "API is running"}), 200

@app.route('/uploads', methods=['POST'])
def upload():
    """
    Verarbeitet hochgeladene Bilder und generiert ein neues Bild
    mit Stable Diffusion XL (Base) unter Berücksichtigung verschiedener Stile.
    Unterstützt neben 'anime', 'manga', 'real' auch 'popart', 'watercolor',
    'oilpaint' und einen freien 'custom' Stil.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Kein Bild hochgeladen"}), 400

    file = request.files['file']
    style = request.form.get('style', "anime").lower()
    custom_prompt = request.form.get('customPrompt', '').strip()

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Öffne das hochgeladene Bild und passe es an die empfohlene Größe an
        try:
            init_image = Image.open(filepath).convert("RGB")
            init_image = init_image.resize(MAX_SIZE, Image.LANCZOS)
        except Exception as e:
            return jsonify({"error": f"Fehler beim Öffnen/Verarbeiten des Bildes: {str(e)}"}), 500

        # Konfiguration für verschiedene Stile
        style_config = {
            "anime": {
                "prompt": (
                    "anime portrait, highly detailed face, studio ghibli style, "
                    "natural skin tones, maintain original likeness, expressive eyes, "
                    "vibrant colors, 8k resolution, sharp focus"
                ),
                "strength": 0.55,
                "guidance": 7.5,
                "negative_prompt": "ugly, deformed face, unrealistic eyes, distorted features",
                "use_mask": True
            },
            "manga": {
                "prompt": (
                    # Prompt für klassisches Manga in Schwarzweiß
                    "1-bit black and white manga style, no color, line art, extremely high contrast, "
                    "thick black outlines, halftone shading, vintage manga vibe, negative space"
                ),
                "strength": 0.45,
                "guidance": 8.0,
                # Unterdrückt Farbe, photorealistische Elemente etc.
                "negative_prompt": "color, pastel, vibrant, bright, realistic, 3d, painting, oil, watercolor",
                "use_mask": False
            },
            "real": {
                "prompt": "photo-realistic, preserve details, neutral lighting",
                "strength": 0.1,
                "guidance": 3.0,
                "negative_prompt": "",
                "use_mask": False
            },
            "popart": {
                "prompt": (
                    "pop art style, bright colors, bold lines, reminiscent of Roy Lichtenstein, "
                    "stylized shading, halftone patterns, black outlines, cartoonish vibe"
                ),
                "strength": 0.6,
                "guidance": 7.5,
                "negative_prompt": "ugly, out of frame, distorted, realism",
                "use_mask": False
            },
            "watercolor": {
                "prompt": (
                    "watercolor painting style, soft edges, fluid brushstrokes, "
                    "subtle color transitions, airy aesthetic, gentle blending, bright pastel palette"
                ),
                "strength": 0.6,
                "guidance": 7.0,
                "negative_prompt": "digital, photorealistic, glitch, text",
                "use_mask": False
            },
            "oilpaint": {
                "prompt": (
                    "oil painting style, reminiscent of classical renaissance painting, "
                    "rich detail, luminous color transitions, visible brushstrokes, strong chiaroscuro, highly detailed face"
                ),
                "strength": 0.65,
                "guidance": 7.5,
                "negative_prompt": "digital, glitch, text, cartoon",
                "use_mask": False
            }
        }

        # Prüfen, ob Style existiert oder ob Custom Prompt verwendet werden soll
        if style in style_config:
            config = style_config[style]
        else:
            # Wenn nicht im style_config und custom_prompt nicht leer -> Custom-Stil
            if custom_prompt:
                config = {
                    "prompt": custom_prompt,
                    "strength": 0.6,
                    "guidance": 7.5,
                    "negative_prompt": "",
                    "use_mask": False
                }
            else:
                return jsonify({"error": f"Unbekannter Stil '{style}' und kein customPrompt übergeben"}), 400

        mask_image = create_face_mask(init_image) if config["use_mask"] else None

        try:
            # Generiere das Bild mit SDXL Img2Img
            result = pipe(
                prompt=config["prompt"],
                negative_prompt=config["negative_prompt"],
                image=init_image,
                mask_image=mask_image,
                strength=config["strength"],
                guidance_scale=config["guidance"],
                num_inference_steps=60
            )

            generated_image = result.images[0]

            # Für Manga-Stil zusätzlich in echte Graustufen umwandeln:
            if style == "manga":
                # Graustufen (8-Bit)
                generated_image = generated_image.convert("L")
                # Alternativ reines Schwarz-Weiß (1-Bit, optional):
                # generated_image = generated_image.convert("1")

            # Speichere das generierte Bild
            output_filename = f"generated_{style}_{filename}"
            output_filepath = os.path.join(app.config['GENERATED_FOLDER'], output_filename)
            generated_image.save(output_filepath)

            # Gebe die URL des generierten Bildes zurück
            generated_image_url = url_for('static', filename=f"generated/{output_filename}", _external=True)
            return jsonify({"generated_image": generated_image_url})

        except Exception as e:
            return jsonify({"error": f"Fehler bei der Bildgenerierung: {str(e)}"}), 500

    else:
        return jsonify({"error": "Ungültige Datei"}), 400

if __name__ == '__main__':
    # Bitte beachte, dass SDXL mehr GPU-Ressourcen erfordert als SD 1.5/2.x
    # Stelle sicher, dass du über genügend VRAM verfügst (idR. mind. 12 GB oder mehr).
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from PIL import Image
import torch
import numpy as np
from diffusers import StableDiffusionXLImg2ImgPipeline

# Flask App initialisieren
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Konfigurationsparameter
UPLOAD_FOLDER = 'static/uploads'
GENERATED_FOLDER = 'static/generated'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Für SDXL sind 1024x1024 oft ein guter Startpunkt (sofern genügend VRAM vorhanden ist)
MAX_SIZE = (1024, 1024)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Max. 10 MB

# Sicherstellen, dass die Ordner existieren
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(GENERATED_FOLDER, exist_ok=True)

# Stable Diffusion XL Modell laden (Base-Modell)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
).to(device)

def allowed_file(filename):
    """Prüft, ob die Datei ein zulässiges Bildformat hat."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_face_mask(image):
    """
    Erstellt eine einfache Gesichtsmaske.
    (Beispielhaft auf einen manuellen Bereich im Bild beschränkt.)
    """
    width, height = image.size
    mask = np.zeros((height, width), dtype=np.uint8)

    # Manueller Bereich für das Gesicht
    face_box = (width // 4, height // 5, width * 3 // 4, height * 3 // 4)
    mask[face_box[1]:face_box[3], face_box[0]:face_box[2]] = 255

    return Image.fromarray(mask)

@app.route('/')
def health_check():
    """Überprüft, ob die API läuft."""
    return jsonify({"message": "API is running"}), 200

@app.route('/uploads', methods=['POST'])
def upload():
    """
    Verarbeitet hochgeladene Bilder und generiert ein neues Bild
    mit Stable Diffusion XL (Base) unter Berücksichtigung verschiedener Stile.
    Unterstützt neben 'anime', 'manga', 'real' auch 'popart', 'watercolor',
    'oilpaint' und einen freien 'custom' Stil.
    """
    if 'file' not in request.files:
        return jsonify({"error": "Kein Bild hochgeladen"}), 400

    file = request.files['file']
    style = request.form.get('style', "anime").lower()
    custom_prompt = request.form.get('customPrompt', '').strip()

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Öffne das hochgeladene Bild und passe es an die empfohlene Größe an
        try:
            init_image = Image.open(filepath).convert("RGB")
            init_image = init_image.resize(MAX_SIZE, Image.LANCZOS)
        except Exception as e:
            return jsonify({"error": f"Fehler beim Öffnen/Verarbeiten des Bildes: {str(e)}"}), 500

        # Konfiguration für verschiedene Stile
        style_config = {
            "anime": {
                "prompt": (
                    "anime portrait, highly detailed face, studio ghibli style, "
                    "natural skin tones, maintain original likeness, expressive eyes, "
                    "vibrant colors, 8k resolution, sharp focus"
                ),
                "strength": 0.55,
                "guidance": 7.5,
                "negative_prompt": "ugly, deformed face, unrealistic eyes, distorted features",
                "use_mask": True
            },
            "manga": {
                "prompt": (
                    # Prompt für klassisches Manga in Schwarzweiß
                    "1-bit black and white manga style, no color,drawn with a pencil, line art, extremely high contrast, "
                    "thick black outlines, halftone shading, vintage manga vibe, negative space"
                ),
                "strength": 0.45,
                "guidance": 8.0,
                # Unterdrückt Farbe, photorealistische Elemente etc.
                "negative_prompt": "color, pastel, vibrant, bright, realistic, 3d, painting, oil, watercolor",
                "use_mask": False
            },
            "real": {
                "prompt": "photo-realistic, preserve details, neutral lighting",
                "strength": 0.1,
                "guidance": 3.0,
                "negative_prompt": "",
                "use_mask": False
            },
            "popart": {
                "prompt": (
                    "pop art style, bright colors, bold lines, reminiscent of Roy Lichtenstein, "
                    "stylized shading, halftone patterns, black outlines, cartoonish vibe"
                ),
                "strength": 0.6,
                "guidance": 7.5,
                "negative_prompt": "ugly, out of frame, distorted, realism",
                "use_mask": False
            },
            "watercolor": {
                "prompt": (
                    "watercolor painting style, soft edges, fluid brushstrokes, "
                    "subtle color transitions, airy aesthetic, gentle blending, bright pastel palette"
                ),
                "strength": 0.6,
                "guidance": 7.0,
                "negative_prompt": "digital, photorealistic, glitch, text",
                "use_mask": False
            },
            "oilpaint": {
                "prompt": (
                    "oil painting style, reminiscent of classical renaissance painting, "
                    "rich detail, luminous color transitions, visible brushstrokes, strong chiaroscuro, highly detailed face"
                ),
                "strength": 0.65,
                "guidance": 7.5,
                "negative_prompt": "digital, glitch, text, cartoon",
                "use_mask": False
            }
        }

        # Prüfen, ob Style existiert oder ob Custom Prompt verwendet werden soll
        if style in style_config:
            config = style_config[style]
        else:
            # Wenn nicht im style_config und custom_prompt nicht leer -> Custom-Stil
            if custom_prompt:
                config = {
                    "prompt": custom_prompt,
                    "strength": 0.6,
                    "guidance": 7.5,
                    "negative_prompt": "",
                    "use_mask": False
                }
            else:
                return jsonify({"error": f"Unbekannter Stil '{style}' und kein customPrompt übergeben"}), 400

        mask_image = create_face_mask(init_image) if config["use_mask"] else None

        try:
            # Generiere das Bild mit SDXL Img2Img
            result = pipe(
                prompt=config["prompt"],
                negative_prompt=config["negative_prompt"],
                image=init_image,
                mask_image=mask_image,
                strength=config["strength"],
                guidance_scale=config["guidance"],
                num_inference_steps=60
            )

            generated_image = result.images[0]

            # Für Manga-Stil zusätzlich in echte Graustufen umwandeln:
            if style == "manga":
                # Graustufen (8-Bit)
                generated_image = generated_image.convert("L")
                # Alternativ reines Schwarz-Weiß (1-Bit, optional):
                # generated_image = generated_image.convert("1")

            # Speichere das generierte Bild
            output_filename = f"generated_{style}_{filename}"
            output_filepath = os.path.join(app.config['GENERATED_FOLDER'], output_filename)
            generated_image.save(output_filepath)

            # Gebe die URL des generierten Bildes zurück
            generated_image_url = url_for('static', filename=f"generated/{output_filename}", _external=True)
            return jsonify({"generated_image": generated_image_url})

        except Exception as e:
            return jsonify({"error": f"Fehler bei der Bildgenerierung: {str(e)}"}), 500

    else:
        return jsonify({"error": "Ungültige Datei"}), 400

if __name__ == '__main__':
    # Bitte beachte, dass SDXL mehr GPU-Ressourcen erfordert als SD 1.5/2.x
    # Stelle sicher, dass du über genügend VRAM verfügst (idR. mind. 12 GB oder mehr).
    app.run(host='0.0.0.0', port=5000, debug=True)