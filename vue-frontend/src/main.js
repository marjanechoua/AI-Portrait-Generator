import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Import router
import '@fortawesome/fontawesome-free/css/all.min.css';


const app = createApp(App);
app.use(router); // Tell Vue to use the router
app.mount('#app');
