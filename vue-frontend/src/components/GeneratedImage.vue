<template>
    <div v-if="image" id="result">
        <img :src="image" alt="Generated Portrait" />
        <a :href="image" download="generated_image.png" id="download-button">Download</a>
    </div>
</template>

<script>
export default {
    name: 'GeneratedImage',
    props: {
        image: String
    }
};
</script>

<style scoped>
#result img {
    max-width: 100%;
    height: auto;
}

#download-button {
    display: block;
    text-align: center;
    margin-top: 20px;
    color: #4caf50;
    text-decoration: none;
}

#download-button:hover {
    text-decoration: underline;
}
</style>
