// Composables
import { createRouter, createWebHistory } from 'vue-router'
import {store} from "@/store";


const routes = [
  {
    path: '/',
    name: '*',
    component: () => import('@/views/LoginPage.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginPage.vue'),
  },
  {
    path: '/profile',
    name: 'profile',
    meta: {
      requiresLogin: true
    },
    component: () => import('@/views/ProfilePage.vue'),
  },
  {
    path: '/services',
    name: 'services',
    meta: {
      requiresLogin: true
    },
    component: () => import('@/views/ServicesPage.vue'),
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
