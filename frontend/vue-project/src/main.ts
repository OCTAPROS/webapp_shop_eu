import { registerPlugins } from '@/plugins'
import App from './App.vue'
import { createApp } from 'vue'

export const BASE_URL: string = 'http://localhost:8001'

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
