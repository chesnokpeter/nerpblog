import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { VitePWA } from 'vite-plugin-pwa'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(), 
    VitePWA({
      devOptions: {
        enabled: true
      },
      includeAssets: ['public/favicon.ico', 'public/apple-touch-icon.png', 'public/favicon.svg'],
      manifest: {
        name: 'nerpblog',
        short_name: 'nerpblog',
        description: 'nerpblog is a OpenSource post publishing',
        theme_color: '#ffffff',
        icons: [
          {
            src: 'pwa-192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'pwa-512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ],screenshots: [ 
        { 
          src: "mobile.jpg", 
          type: "image/jpeg", 
          sizes: "573x1280", 
          form_factor: "narrow" 
        } 
      ],prefer_related_applications: false
      },
    })
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
