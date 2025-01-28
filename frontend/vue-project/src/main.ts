import { registerPlugins } from '@/plugins'
import { createApp } from 'vue'
import App from './App.vue'

export const BASE_URL: string = 'http://localhost:8001'

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
