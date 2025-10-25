import { createRouter, createWebHistory } from 'vue-router'
import ScannerPage from '@/pages/ScannerPage.vue'
import ProductPage from '@/pages/ProductPage.vue'
import OptimizerPage from '@/pages/OptimizerPage.vue'

const routes = [
  { path: '/', redirect: '/scanner' },
  { path: '/scanner', name: 'scanner',component: ScannerPage },
  { path: '/product/:barcode', component: ProductPage, props: true },
  { path: '/optimize', name: 'optimize', component: OptimizerPage },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
