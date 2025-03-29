<template>
    <section class="cta">
        <h2>Ready to Create Your Own Portrait?</h2>
        <p>Start transforming your photos today! It's fast, easy and fun.</p>
        <div class="cta-buttons">
            <router-link to="/create">
                <button class="primary-btn">Upload Your Photo</button>
            </router-link>
            <router-link to="/about">
                <button class="secondary-btn">Learn More</button>
            </router-link>
        </div>
    </section>
</template>

<script>
export default {
    name: 'CTA'
};
</script>

<style scoped>
.cta {
    text-align: center;
    padding: 40px;
    background-color: #2b5d6e;
    color: white;
}

.cta h2 {
    margin-top: 10px;
    font-size: 1.8rem;
}

.cta-buttons {
    margin-top: 20px;
    margin-bottom: 15px;
}

.primary-btn {
    /* background-color: #fff; */
    /* color: #3f8ca0; */
    color:  #202020;
    padding: 10px 40px;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    font-size: 0.9rem;
    margin-right: 10px;
}

/*
.primary-btn:hover {
    background-color: #77cde0;
    color: white;
}
*/

.secondary-btn {
    /* background-color: transparent; */
    /* color: #fff; */
    color:  #202020;
    border: none;
    padding: 10px 25px;
    cursor: pointer;
    border-radius: 8px;
    font-size: 0.9rem;
}

</style>
