<script>

import CTA from '../components/CTA.vue';
import Footer from '../components/Footer.vue';

export default {
    name: 'AboutView',
    components: {

        CTA,
        Footer
    }
};
</script>

<template>
    <div class="about-us">
        <!-- Hero Section -->
        <section class="hero">
            <div class="hero-content">
                <h1>About Portrait Generator</h1>
                <p>
                    Learn more about how we built the AI-powered tool transforming your photos into art.
                </p>
            </div>
        </section>

        <!-- Project Overview Section -->
        <section class="section project-overview">
            <h2>What is Portrait Generator?</h2>
            <p>
                Portrait Generator is an AI-powered web application that allows users to turn photos into beautiful,
                personalized artwork in various styles. Whether you're looking for a realistic portrait or a creative
                art piece, our tool makes it easy.
            </p>
            <div class="images">
                <img alt="Before" src="@/assets/before.png"/>
                <img alt="After" src="@/assets/after.png"/>
            </div>

        </section>

        <!-- Inspiration & Vision Section -->
        <section class="section inspiration">
            <div class="section-header">
                <h2>Our Inspiration</h2>
            </div>
            <div class="inspiration-content">
                <div class="text">
                    <p>
                        Inspired by popular portrait tools like CapCut and Canva, we wanted to push the boundaries of AI
                        image generation to offer more artistic options, smoother user experience, and faster processing
                        times.
                    </p>
                </div>
                <div class="image">
                    <img alt="Team Inspiration" src="@/assets/inspiration.gif"/>
                </div>
            </div>
        </section>

        <!-- Technology Section -->
        <section class="section tech">
            <h2>The Technology Behind the Magic</h2>
            <p>
                We use cutting-edge technologies like the Stable Diffusion AI model for generating portraits and Python
                (Flask) for the backend. The frontend is built using Vue.js to ensure a smooth, responsive user
                experience.
            </p>
            <div class="tech-stack">
                <div class="tech-item">
                    <i class="fab fa-vuejs"></i>
                    <p>Vue.js</p>
                </div>
                <div class="tech-item">
                    <i class="fab fa-python"></i>
                    <p>Python (Flask)</p>
                </div>
                <div class="tech-item">
                    <i class="fas fa-cogs"></i>
                    <p>Stable Diffusion AI</p>
                </div>
            </div>
        </section>

        <!-- Meet the Team Section (Icons) -->
        <section class="section team">
            <h2>Meet the Team</h2>
            <div class="team-member-card">
                <!-- Frontend Developer 1 -->
                <div class="team-member">
                    <i class="fas fa-laptop-code"></i> <!-- Frontend Developer Icon -->
                    <div class="info">
                        <h3>Selin Ünal</h3>
                        <p>Frontend Developer</p>
                    </div>
                </div>
                <!-- Frontend Developer 2 -->
                <div class="team-member">
                    <i class="fas fa-laptop-code"></i> <!-- Frontend Developer Icon -->
                    <div class="info">
                        <h3>Marjane Choua</h3>
                        <p>Frontend Developer</p>
                    </div>
                </div>
                <!-- Backend Developer 1 -->
                <div class="team-member">
                    <i class="fas fa-server"></i> <!-- Backend Developer Icon -->
                    <div class="info">
                        <h3>Musa Jabbarli</h3>
                        <p>Backend Developer</p>
                    </div>
                </div>
                <!-- Backend Developer 2 -->
                <div class="team-member">
                    <i class="fas fa-server"></i> <!-- Backend Developer Icon -->
                    <div class="info">
                        <h3>Victor-Andrei Bestea</h3>
                        <p>Backend Developer</p>
                    </div>
                </div>
            </div>
        </section>







        <!-- Call to Action Section -->
            <CTA />

        <!-- Footer Section -->
            <Footer />
        
    </div>
</template>

<script setup>

import { useRouter } from 'vue-router';


const router = useRouter();

const goToHomePage = () => {
    router.push('/');
};
</script>

<style scoped>
.about-us {
    font-family: 'Arial', sans-serif;
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

/* Section Styles */
.section {
    padding: 50px 20px;
}

.project-overview h2,
.inspiration h2,
.tech h2,
.team h2 {
    font-size: 2.5rem;
    color: #333;
    margin-bottom: 20px;
}

.project-overview p,
.inspiration p,
.tech p {
    font-size: 1.1rem;
    color: #555;
    margin-bottom: 30px;
}

.image-example {
    max-width: 100%;
    border-radius: 8px;
}

.images {
    display: flex; /* Bilder nebeneinander anordnen */
    gap: 40px; /* Abstand zwischen den Bildern */
}

.images img {
    width: 100%;
    max-width: 400px; /* Maximale Breite */
    height: auto; /* Automatische Skalierung für gleiche Höhe */
    transition: transform 0.3s ease-in-out; /* Smooth Hover Effekt */
}

.images img:hover {
    transform: scale(1.05); /* Leicht vergrößern beim Hoover */
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2); /* Optional: Schatten für mehr Effekt */
}

.inspiration-content {
    display: flex;
    justify-content: space-between;
    gap: 30px;
    align-items: center; /* Zentriert Text und Bild vertikal */
}

.inspiration-content .text {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center; /* Stellt sicher, dass der Text vertikal ausgerichtet ist */
    margin-top: -10px; /* Hebt den Text leicht nach oben */
}

.inspiration-content .image {
    flex: 1;
}

.inspiration img {
    width: 90%;
    margin-left: 30px;
}

.tech-stack {
    display: flex;
    justify-content: space-around;
    gap: 40px;
    margin-top: 40px;
    color: #2b5d6e;
}

.tech-item {
    text-align: center;
}


.tech-item i {
    
    margin-bottom: 10px;
    font-size: 5rem;
        
}

.team-member-card {
    display: flex;
    justify-content: space-around;
    gap: 40px;
    margin-top: 30px;
}

.team-member {
    width: 200px;
    text-align: center;
    border-radius: 8px;
    box-shadow: 0 0 10px #1E3A46;
    padding: 20px;
    transition: transform 0.3s;
}

.team-member img {
    width: 100%;
    border-radius: 50%;
    margin-bottom: 15px;
}

.team-member:hover {
    transform: translateY(-10px);
}

.team-member h3 {
    font-size: 1.2rem;
    margin-bottom: 5px;
}

.team-member p {
    font-size: 1rem;
    color: #555;
}

.CTA .cta-buttons {
    display: none !important;
}

</style>