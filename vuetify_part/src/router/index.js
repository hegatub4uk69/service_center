// Composables
import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  /*{
    path: '/',
    name: '*',
    component: () => import('@/views/Reg_Log.vue'),
  },*/
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/Reg_Log.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
