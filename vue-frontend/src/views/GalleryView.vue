<template>
    <section>
        <GalleryComponent />
        <Footer />
    </section>
</template>

<script>
import GalleryComponent from '../components/Gallery.vue';
import Footer from '../components/Footer.vue';

export default {
    name: 'GalleryView',
    components: {
        GalleryComponent,
        Footer
    }
};
</script>