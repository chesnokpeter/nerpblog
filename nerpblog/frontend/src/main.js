// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import VueSplide from '@splidejs/vue-splide';


import router from './router'

const app = createApp(App)

app.use(router)
app.use(VueSplide)
app.mount('#app')
