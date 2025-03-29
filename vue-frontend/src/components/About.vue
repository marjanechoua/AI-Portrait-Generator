<template>
    <section class="about">
        <h2>What We Do</h2>
        <p>We use cutting-edge AI technology to transform your photos into beautiful, artistic portraits.</p>
        <div class="process">
            <div class="step">
                <i class="fas fa-cloud-upload-alt"></i>
                <p>Upload your photo</p>
            </div>
            <div class="step">
                <i class="fas fa-palette"></i>
                <p>Select a style</p>
            </div>
            <div class="step">
                <i class="fas fa-download"></i>
                <p>Download your portrait</p>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'About'
};
</script>

<style scoped>
.about {
    background-color: #fff;
    padding: 40px;
    text-align: center;
}

.about h2 {
    font-size: 1.8rem;
}

.process {
    display: flex;
    justify-content: space-around;
    margin-top: 40px;
}

.step img {
    width: 50px;
    height: 50px;
}

.step i {
    font-size: 50px;
    color: #2b5d6e; /* #3f8ca0; */
    margin-bottom: 10px;
}

</style>
