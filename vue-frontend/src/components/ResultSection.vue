<template>
    <div v-if="loading" class="loading-spinner">Loading...</div>
    <div v-else-if="image" class="result">
        <img :src="image" alt="Generated Image" />
        <a :href="image" download="generated-image.png">Download</a>
    </div>
    <div v-else class="no-result">No result available</div>
</template>

<script>
export default {
    name: 'ResultSection',
    props: {
        image: String,
        loading: Boolean
    }
};
</script>
