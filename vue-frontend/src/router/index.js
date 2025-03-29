import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomeView.vue';
import Generate from '../views/GenerateView.vue';
import Gallery from '../views/GalleryView.vue';
import About from '../views/AboutView.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/create', component: Generate },
  { path: '/gallery', component: Gallery },
  { path: '/about', component: About }
];

const router = createRouter({
  history: createWebHistory(), // This uses HTML5 history mode
  routes
});

export default router;
