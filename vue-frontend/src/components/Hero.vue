<template>
    <section class="hero">
        <div class="carousel">
            <!-- Carousel Component -->
        </div>
        <div class="hero-text">
            <h1>Transform Your Portraits into Stunning AI Art</h1>
            <p>Upload your photo, choose a style and let our AI work it's magic.</p>
            <div class="cta-buttons">
                <router-link to="/create">
                    <button class="primary-btn">Get Started</button>
                </router-link>
                <router-link to="/gallery">
                    <button class="secondary-btn">Explore Examples</button>
                </router-link>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Hero'
};
</script>

<style scoped>
.hero {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 500px;
    background-color: #2b5d6e; /* grau f4f4f4 */
}

.hero-text {
    max-width: 50%;
    padding: 50px;
    color: #ffffff;
}

.hero-text h1 {
    font-size: 2.5rem;
    color: #ffffff; /* schwarz #333 */
}

.cta-buttons {
    display: flex;
    gap: 10px;
    margin-top: 30px;
}

.primary-btn {
    /* background-color: #3f8ca0; */
    /* color: white; */
    color:  #202020;
    padding: 10px 60px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
}

/*
.primary-btn:hover {
    background-color: #77cde0;
    color: white;
}
*/

.secondary-btn {
    padding: 10px 25px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9rem;
    color:  #202020;
}
</style>
