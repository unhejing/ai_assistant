import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Playground from '../views/Playground.vue'

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/playground', name: 'playground', component: Playground },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router