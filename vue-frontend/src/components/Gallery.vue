<template>
    <section class="gallery" id="gallery">
        <!-- Title of the Gallery Section -->
        <h2>See the Magic in Action</h2>
        <p>Explore stunning before-and-after portraits and read what others say about their AI-enhanced results.</p>

        <!-- Gallery Grid -->
        <div class="gallery-grid">
            <!-- Loop through portraits array to display each one -->
            <div v-for="(portrait, index) in portraits" :key="index" class="gallery-item">

                <!-- Image Comparison (Before and After) -->
                <div class="image-container">
                    <!-- Use the method to get the correct image path -->
                    <img :src="getImagePath(portrait.before)" alt="Before" class="before" />
                    <img :src="getImagePath(portrait.after)" alt="After" class="after" />
                </div>

                <!-- Image Caption (optional description) -->
                <div class="caption">
                    <p class="caption-text">Before & After</p>
                </div>

                <!-- User Testimonial Section -->
                <div class="testimonial">
                    <p class="testimonial-quote">"Amazing transformation! The results exceeded my expectations!"</p>
                    <div class="rating">
                        <span>⭐⭐⭐⭐⭐</span> <!-- 5-star rating -->
                    </div>
                    <p class="user-name">- John Doe</p>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'Gallery',
    data() {
        return {
            portraits: [
                {
                    before: 'image.png',        // Image inside 'src/assets'
                    after: 'image_generated.png'
                },
                {
                    before: 'before2.jpg',      // Image inside 'src/assets'
                    after: 'after2.jpg'
                },
                // Add more portrait objects as necessary
            ]
        };
    },
    methods: {
        // Method to resolve the image paths dynamically using Vite's import.meta.url
        getImagePath(image) {
            // This makes sure Vite correctly resolves the image path
            return new URL(`../assets/${image}`, import.meta.url).href;
        }
    }
};
</script>

<style scoped>
/* Gallery Section */
.gallery {
    padding: 40px 20px;
    background-color: #f9f9f9;
    text-align: center;
}

.gallery h2 {
    font-size: 1.8rem;
    /* color: #333; */
    /* margin-bottom: 40px; */
    font-weight: bold;
}

/* Gallery Grid with responsive layout */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    justify-items: center;
    margin-top: 50px;
}

/* Gallery Item Styling */
.gallery-item {
    position: relative;
    overflow: hidden;
    display:flex;
    flex-direction:column;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
}

/* Image Container */
.image-container {
    position: relative;
    display: flex;
    justify-content: space-between;
    gap: 10px;
    width:100%;
    overflow: hidden;
}

.image-container img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 8px;
    transition: transform 0.3s ease;
}

.image-container img.before {
    opacity: 1;
}

.image-container img.after {
    opacity: 0;
    position: absolute;
    top: 0;
    left: 0;
    transition: opacity 0.5s ease;
}

/* Hover Effects for Before/After Comparison */
.gallery-item:hover .image-container img.before {
    opacity: 0;
}

.gallery-item:hover .image-container img.after {
    opacity: 1;
}

/* Image Caption Styling */
.caption {
    margin-top: 15px;
}

.caption-text {
    font-size: 1rem;
    color: #555;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 10px;
}

/* Testimonial Section Styling */
.testimonial {
    margin-top: 20px;
    background-color: #f1f1f1;
    padding: 15px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.testimonial-quote {
    font-size: 1rem;
    color: #444;
    font-style: italic;
    margin-bottom: 10px;
}

.rating {
    color: #f9c74f;
    font-size: 1.2rem;
}

.user-name {
    font-weight: bold;
    font-size: 0.9rem;
    color: #333;
}
</style>
