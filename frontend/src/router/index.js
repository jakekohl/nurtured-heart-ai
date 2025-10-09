import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Generator',
    component: () => import('../views/GeneratorView.vue')
  },
  {
    path: '/what-is-nha',
    name: 'WhatIsNHA',
    component: () => import('../views/WhatIsNHA.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/AboutView.vue')
  },
  {
    path: '/faq',
    name: 'FAQ',
    component: () => import('../views/FAQView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

