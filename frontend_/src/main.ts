import { createApp } from "vue";
import App from "./App.vue";

import "~/styles/index.scss";
import "element-plus/theme-chalk/src/message.scss"
import "font-logos/assets/font-logos.css" 



import ElementPlus from 'element-plus'
import { createPinia } from 'pinia';  
import router from './router'

const app = createApp(App);

app.use(ElementPlus).use(createPinia()).use(router).mount('#app')