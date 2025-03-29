<template>
  <header class="header">
    <!-- Logo Section -->
    <div class="logo">
      <div>
        <img alt="Logo" src="@/assets/Logo.jpeg" /> <!-- Use your actual logo path here -->
      </div>
    </div>
    <!-- Navigation Section -->
    <nav>
      <ul>
        <li><router-link to="/" exact-active-class="active-link">Home</router-link></li>
        <li><router-link to="/create" exact-active-class="active-link">Create Portraits</router-link></li>
        <li><router-link to="/gallery" exact-active-class="active-link">Gallery</router-link></li>
        <li><router-link to="/about" exact-active-class="active-link">About Us</router-link></li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header'
};
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  margin-right: 15px;
  background-color: #ffffff;
}

.logo img {
  height: 80px;
  object-fit: contain;
}

nav ul {
  display: flex;
  gap: 40px;
  list-style-type: none;
  padding: 0;
  margin: 0;
}

nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: color 0.3s;
}

li {
  font-size: 1.2rem;
}

li:hover {
    transform: scale(1.05);
    transition: border 0.3s ease;
}

.active-link {
  font-weight: bold;
  color: #3f8ca0;
  border-bottom: 3px solid #3f8ca0;
  padding-bottom: 5px;
}

.cta-btn {
  background-color: #3f8ca0;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-weight: bold;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.cta-btn:hover {
  background-color: #77cde0;
}

</style>