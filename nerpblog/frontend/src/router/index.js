// import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView
//     },
//     {
//       path: '/about',
//       name: 'about',
//       // route level code-splitting
//       // this generates a separate chunk (About.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import('../views/AboutView.vue')
//     }
//   ]
// })

// export default router


import { createRouter, createWebHistory } from 'vue-router'
import ProgView from '../views/ProgView.vue'
import MainView from '../views/MainView.vue'
import AboutView from '../views/AboutView.vue'
import PostView from '../views/PostView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: MainView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/prog',
      name: 'prog',
      component: ProgView
    },
    {
      path: '/:id',
      name: 'post',
      component: PostView, 
      props: route => ({ id: Number(route.params.id) })
    }
  ]
})

export default router
