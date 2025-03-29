<template>
    <div class="generate-portrait">
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-content">
                <h1>Turn Your Photo Into Art</h1>
                <p>Upload your image and choose a style to create a unique artwork.</p>
            </div>
        </section>

        <!-- Main Content Area -->
        <div class="main-content">
            <!-- Content Layout: Left side for upload and preview, Right side for style selection -->
            <div class="content-layout">
                <!-- Left Column: Upload & Preview -->
                <div class="left-column">
                    <!-- Image Upload Section -->
                    <section class="upload-section">
                        <h2>Upload Your Image</h2>
                        <div class="upload-area" @click="triggerFileInput">
                            <input type="file" ref="fileInput" accept="image/*" @change="handleFileChange" />
                            <p>Drag and drop your image or click to upload</p>
                        </div>
                        <div v-if="previewImage" class="image-preview">
                            <img :src="previewImage" alt="Preview" />
                        </div>
                    </section>

                    <!-- Result Section -->
                    <section v-if="generatedImage" class="result-section">
                        <h2>Your Artistic Portrait</h2>
                        <img :src="generatedImage" alt="Generated Portrait" />
                        <a :href="generatedImage" download="portrait.png" class="download-btn">Download Portrait</a>
                    </section>
                </div>

                <!-- Right Column: Style Selection -->
                <div class="right-column">
                    <section class="style-selection">
                        <h2>Choose a Style</h2>
                        <div class="style-options">
                            <div v-for="style in styles" :key="style.name" class="style-card"
                                @click="selectStyle(style)" :class="{ selected: selectedStyle === style.name }">
                                <img :src="style.image" :alt="style.name" />
                                <p>{{ style.name }}</p>
                            </div>
                        </div>
                        <div class="custom-style-input">
                            <label for="customStyle">Or enter your own style: </label>
                            <input type="text" id="customStyle" v-model="customStyle"
                                placeholder="e.g. Cyberpunk portrait" />
                        </div>
                    </section>

                    <!-- Apply Style Button -->
                    <section class="apply-section">
                        <button v-if="selectedFile && (selectedStyle || customStyle)" @click="applyStyle"
                            class="apply-btn">
                            Apply Style
                        </button>
                    </section>
                </div>
            </div>

            <!-- Loading Spinner -->
            <div v-if="isProcessing" class="loading">
                <p>Processing...</p>
            </div>
        </div>
    </div>
    <footer>
        <Footer/>
    </footer>
</template>

<script>
import { ref } from "vue";
import Footer from '../components/Footer.vue';
import AnimeImage from "@/assets/Anime.png";
import MangaImage from "@/assets/Manga.png";
import RealImage from "@/assets/Real.png";
import PopArtImage from "@/assets/PopArt.jpg";
import OilPaintImage from "@/assets/OilPaint.jpg";
import WaterColorImage from "@/assets/WaterColor.jpg";


export default {
    name: "GeneratePortrait",
    components: {
        Footer
    },
    setup() {
        const selectedFile = ref(null);
        const selectedStyle = ref("");
        const customStyle = ref("");
        const previewImage = ref(null);
        const generatedImage = ref(null);
        const isProcessing = ref(false);

        const styles = ref([
            { name: "Anime", image: AnimeImage },
            { name: "Manga", image: MangaImage },
            { name: "Real", image: RealImage },
            { name: "Pop Art", image: PopArtImage },
            { name: "Watercolor", image: WaterColorImage },
            { name: "Oil Paint", image: OilPaintImage }
            
            
            
        ]);

        const triggerFileInput = () => {
            document.querySelector('input[type="file"]').click();
        };

        const handleFileChange = (event) => {
            const file = event.target.files[0];
            if (file) {
                selectedFile.value = file;
                previewImage.value = URL.createObjectURL(file);
            }
        };

        const selectStyle = (style) => {
            selectedStyle.value = style.name;
            customStyle.value = "";
        };
        const applyStyle = async () => {
            if (!selectedFile.value || (!selectedStyle.value && !customStyle.value)) {
                alert("Please upload an image and select or enter a style.");
                return;
            }

            isProcessing.value = true;

            const formData = new FormData();
            formData.append("file", selectedFile.value);
            formData.append("style", selectedStyle.value || "custom");
            formData.append("customPrompt", customStyle.value); // <-- Custom Prompt wird jetzt explizit gesendet

            try {
                const response = await fetch("http://localhost:5000/uploads", {
                    method: "POST",
                    body: formData,
                });

                if (!response.ok) {
                    throw new Error("Failed to apply style.");
                }

                const data = await response.json();
                generatedImage.value = data.generated_image; // URL of the generated image
            } catch (error) {
                console.error("Error applying style:", error);
                alert("Error during processing.");
            } finally {
                isProcessing.value = false;
            }
        };


        
        

        return {
            selectedFile,
            selectedStyle,
            customStyle,
            previewImage,
            generatedImage,
            isProcessing,
            styles,
            triggerFileInput,
            handleFileChange,
            selectStyle,
            applyStyle,
        };
    },
};
</script>


<style scoped>
/* Root Style */
.generate-portrait {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    background-color: #f9f9f9;
    color: #333;
    width: 100%;
    margin: 0;
    padding: 0;
}

/* Hero Section */
.hero {
    background: #2b5d6e;
    padding: 50px 20px;
    text-align: center;
    color: white;
}

.hero-content {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 20px;
    color: #ffffff;
}

.hero h1 {
    font-size: 2.5rem;
    margin-bottom: 30px;
}

.hero p {
    font-size: 1rem;
    margin: 10px 0;
}

.cta-btn {
    background-color: #fff;
    color: #2b5d6e;
    padding: 12px 25px;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    margin-top: 20px;
    margin-right: 15px;
    transition: background-color 0.3s;
}

.cta-btn:hover {
    background-color: #2b5d6e;
    color: white;
}

/* Main Content */
.main-content {
    display: flex;
    justify-content: space-between;
    padding: 30px 20px;
    /* Reduced padding */
    flex-wrap: wrap;
}

/* Content Layout: Two Columns */
.content-layout {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
    gap: 20px;
    /* Reduced gap between columns */
}

.left-column {
    flex: 0 0 48%;
    display: flex;
    flex-direction: column;
}

.right-column {
    flex: 0 0 48%;
}

/* Upload Section */
.upload-section {
    background-color: white;
    padding: 25px;
    /* Reduced padding */
    border-radius: 10px;
    /* Slightly smaller border-radius */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    /* Reduced margin */
    text-align: center;
}

.upload-section h2 {
    font-size: 1.4rem;
    /* Reduced font size */
    margin-bottom: 40px;
    /* Reduced margin */
}

.upload-area {
    background-color: #f0f0f0;
    padding: 20px;
    /* Reduced padding */
    border-radius: 8px;
    border: 2px dashed #2b5d6e;
    cursor: pointer;
    text-align: center;
    transition: background-color 0.1s ease;
}

.upload-area:hover {
    background-color:rgb(219, 219, 219);
}

.upload-area input {
    display: none;
}

.image-preview img {
    max-width: 100%;
    border-radius: 8px;
    margin-top: 10px;
    /* Reduced margin */
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Style Selection */
.style-selection {
    background-color: white;
    padding: 25px;
    /* Reduced padding */
    border-radius: 10px;
    /* Slightly smaller border-radius */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
    /* Reduced margin */
}

.style-selection h2 {
    font-size: 1.4rem;
    /* Reduced font size */
    margin-bottom: 40px;
    /* Reduced margin */
    text-align: center;
}

.style-options {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
    gap: 15px;
}

.style-card {
    text-align: center;
        cursor: pointer;
        transition: transform 0.1s ease;
        border-radius: 8px;       
}

.style-card:hover {
    transform: scale(1.05);
}

.style-card img {
    width: 100%;
        height: 140px;
        object-fit: cover;
        border-radius: 8px;
        transition: border 0.1s ease;
}

.style-card p {
    font-size: 1rem;
    margin-top: 5px;
}

.style-card.selected img {
    border: 3px solid #3f8ca0;
}

.custom-style-input input {
    width: 100%;
    max-width: 350px;
    /* Reduced max-width */
    padding: 10px;
    /* Reduced padding */
    font-size: 1rem;
    margin-top: 15px;
    /* Reduced margin */
    border: 2px solid #3f8ca0;
    border-radius: 6px;
    /* Smaller border-radius */
    outline: none;
    transition: border-color 0.3s;
}

.custom-style-input input:focus {
    border-color: #2b5d6e;
}

/* Apply Button */
.apply-section {
    text-align: center;
    margin-top: 20px;
    /* Reduced margin */
}

.apply-btn {
    background-color: #2b5d6e;
    color: white;
    padding: 10px 20px;
    /* Reduced padding */
    font-size: 1.1rem;
    /* Slightly smaller font size */
    border-radius: 6px;
    /* Smaller border-radius */
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

.apply-btn:hover {
    background-color: #3f8ca0;
}

/* Result Section */
.result-section {
    text-align: center;
    margin-top: 20px;
    /* Reduced margin */
}

.result-section img {
    max-width: 100%;
    max-height: 400px;
    /* Reduced max-height */
    border-radius: 10px;
    /* Slightly smaller border-radius */
}

.download-btn {
    display: inline-block;
    margin-top: 20px;
    font-size: 0.9rem;
    /* Reduced font size */
    text-decoration: none;
    background-color: #2b5d6e;
    color: white;
    padding: 10px 22px;
    /* Reduced padding */
    border-radius: 6px;
    /* Smaller border-radius */
}

.download-btn:hover {
    background-color: #2b5d6e;
}

/* Loading */
.loading {
    text-align: center;
    font-size: 1.1rem;
    /* Reduced font size */
    font-weight: 600;
    color: #2b5d6e;
}

/* Responsive Design */
@media (max-width: 768px) {
    .content-layout {
        flex-direction: column;
    }

    .left-column,
    .right-column {
        flex: 1 1 100%;
    }

    .style-options {
        grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
        /* Adjust grid items for smaller screens */
    }
}
</style>