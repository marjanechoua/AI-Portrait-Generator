<template>
    <div class="generate-view-container">
        <div class="main-content">
            <h1>Free AI Portrait Generator</h1>
            <p>
                Erstellen Sie mit unserem kostenlosen KI-Portraitgenerator atemberaubende,
                personalisierte Portraits, die auf Ihren einzigartigen Stil zugeschnitten sind!
            </p>

            <ImageUpload @file-chosen="handleImageUpload" />

            <StyleSelection @style-selected="handleStyleSelection" />

            <button v-if="image && selectedStyle" @click="applyStyle" class="apply-style-button">
                Apply Style
            </button>

            <ResultSection :image="generatedImage" :loading="isProcessing" />
        </div>
    </div>
</template>

<script>
import { ref } from "vue";
import ImageUpload from '../components/ImageUpload.vue';
import StyleSelection from '../components/StyleSelection.vue';
import ResultSection from '../components/ResultSection.vue';

export default {
    name: 'GenerateView',
    components: {
        ImageUpload,
        StyleSelection,
        ResultSection
    },
    setup() {
        const image = ref(null);
        const selectedStyle = ref(null);
        const generatedImage = ref(null);
        const isProcessing = ref(false);

        const handleImageUpload = (uploadedImage) => {
            image.value = uploadedImage;
        };

        const handleStyleSelection = (style) => {
            selectedStyle.value = style;
        };

        const applyStyle = async () => {
            if (!image.value || !selectedStyle.value) return;

            isProcessing.value = true;

            const formData = new FormData();
            formData.append('image', image.value);
            formData.append('style', selectedStyle.value);

            try {
                const response = await fetch('YOUR_BACKEND_URL/api/generate-portrait', {
                    method: 'POST',
                    body: formData,
                    headers: {
                        // You can add headers if necessary (e.g., for authentication)
                        // 'Authorization': 'Bearer YOUR_TOKEN'
                    },
                });

                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }

                const data = await response.json();

                if (data.generated_image) {
                    generatedImage.value = data.generated_image;
                } else {
                    console.error("Error in response data:", data);
                }
            } catch (error) {
                console.error("Error applying style:", error);
            } finally {
                isProcessing.value = false;
            }
        };

        return {
            image,
            selectedStyle,
            generatedImage,
            isProcessing,
            handleImageUpload,
            handleStyleSelection,
            applyStyle
        };
    }
};
</script>

<style scoped>
.generate-view-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px;
}

.main-content {
    max-width: 900px;
    width: 100%;
}

h1 {
    font-size: 2rem;
    margin-bottom: 10px;
}

footer {
    margin-top: 20px;
    text-align: center;
}

.apply-style-button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.apply-style-button:hover {
    background-color: #45a049;
}
</style>
