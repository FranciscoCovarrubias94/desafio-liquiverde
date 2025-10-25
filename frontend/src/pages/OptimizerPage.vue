<template>
  <div>
    <h2 class="text-h5 mb-4">Optimizar Lista</h2>

    <v-text-field
      v-model.number="budget"
      label="Presupuesto máximo ($)"
      prepend-inner-icon="mdi-currency-usd"
      class="mb-3"
    />

    <v-list>
      <v-list-item
        v-for="(item, index) in products"
        :key="index"
        :title="item.name"
        :subtitle="`${item.brand || ''} — $${item.price}`"
      />
    </v-list>

    <v-btn color="green-darken-2" class="mt-4" @click="optimizeList">
      Optimizar Compra
    </v-btn>

    <div v-if="optimized.length" class="mt-6">
      <h3 class="text-h6 mb-2">Resultado Optimizado</h3>
      <v-list>
        <v-list-item
          v-for="(item, index) in optimized"
          :key="index"
          :title="item.name"
          :subtitle="`$${item.price}`"
        />
      </v-list>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const products = ref<any[]>([])
const optimized = ref<any[]>([])
const budget = ref<number>(10.0) // valor inicial

onMounted(() => {
  const stored = localStorage.getItem('product_list')
  products.value = stored ? JSON.parse(stored) : []
})

async function optimizeList() {
  try {
    const response = await axios.post('http://localhost:8000/api/v1/optimize', {
      products: products.value,
      budget: budget.value,
    })
    optimized.value = response.data.optimized
  } catch (err) {
    console.error('Error al optimizar', err)
  }
}
</script>
