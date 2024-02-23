import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
// import { Splide, SplideSlide } from '@splidejs/vue-splide';
// import VueSplide from '@splidejs/vue-splide';



// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:9001',
      }, '/media': {
        target: 'http://localhost:9001',
      }, '/icons': {
        target: 'http://localhost:9001',
    },
  }
}})
