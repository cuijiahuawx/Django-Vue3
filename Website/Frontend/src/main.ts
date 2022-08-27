import { createApp } from 'vue'
import App from './App.vue'

import router from './router' // 引入路由
import { createPinia } from 'pinia' // 引入Pinia存储
import piniaPersist from 'pinia-plugin-persist' // Pinia持久化
import naive from 'naive-ui'  // 引入Naive组件库
import { setupRouterGuard } from '~/router/guard/index'

const pinia = createPinia()
pinia.use(piniaPersist)
const app = createApp(App)

app.use(naive).use(pinia).use(router)
setupRouterGuard(router)

app.mount('#app')
