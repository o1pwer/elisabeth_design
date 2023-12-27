import { createApp } from 'vue';
import App from './App.vue';
import router from './routers/router'; // your router setup
createApp(App).use(router).mount('#app');
