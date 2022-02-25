import { createApp } from 'vue'
import App from './App.vue'
import router from './router' // 引入路由
import { createPinia } from 'pinia' // 引入Pinia存储
import naive from 'naive-ui'  // 引入Naive组件库
import 'vfonts/Lato.css'  // 引入字体
import 'vfonts/FiraCode.css'  // 等宽字体


const app = createApp(App)


app.use(naive).use(createPinia()).use(router)
app.mount('#app')
