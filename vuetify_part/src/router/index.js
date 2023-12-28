// Composables
import {createRouter, createWebHistory} from 'vue-router'
import {store} from "@/store";
import API from "@/axios";

const routes = [
  {
    path: '/:pathMatch(.*)*',
    component: () => import('@/components/404NotFound.vue'),
  },
  {
    path: '/',
    name: 'main',
    redirect: () => {
      return '/login'
    }
  },
  {
    path: '/login',
    name: 'login',
    meta: {
      notLogin: true
    },
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
    path: '/orders',
    name: 'orders',
    meta: {
      requiresLogin: true
    },
    component: () => import('@/views/OrdersPage.vue'),
  },
  {
    path: '/clients',
    name: 'clients',
    meta: {
      requiresLogin: true
    },
    component: () => import('@/views/ClientsPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresLogin)) {
    if (!store.getters.loggedIn) {
      next({name: 'login'})
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.notLogin)) {
    if (localStorage.getItem('token') != null) {
      next({name: 'profile'})
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
