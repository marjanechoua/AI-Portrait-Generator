<template>
    <div>
        
        <Hero />
        <About />
        <Gallery />
        <CTA />
        <Footer />
    </div>
</template>

<script>

import Hero from '../components/Hero.vue';
import About from '../components/About.vue';
import Gallery from '../components/Gallery.vue';
import CTA from '../components/CTA.vue';
import Footer from '../components/Footer.vue';

export default {
    name: 'App',
    components: {
        
        Hero,
        About,
        Gallery,
        CTA,
        Footer
    }
};
</script>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>