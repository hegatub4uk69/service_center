// Composables
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  /*{
    path: '/',
    name: '*',
    component: () => import('@/views/LoginPage.vue'),
  },*/
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginPage.vue'),
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/ProfilePage.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
