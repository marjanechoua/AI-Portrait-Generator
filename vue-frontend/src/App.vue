
<script>
import Header from './components/Header.vue';


export default {
  name: 'App',
  components: {
    Header,
    
  }
};
</script>

<template>
  <div id="app">

    <Header /> <!-- The header with navigation links -->
    
    <router-view /> <!-- This is where the current route's component will be rendered -->
   
  </div>
</template>

<style>

/* Global styles can go here */
</style>
