/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { store } from './store'

// Plugins
import { registerPlugins } from '@/plugins'
import router from "@/router";

const app = createApp(App)

registerPlugins(app)
app.use(router)
app.use(store)
app.mount('#app')

