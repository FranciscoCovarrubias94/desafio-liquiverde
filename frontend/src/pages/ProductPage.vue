<template>
  <div class="p-4">
    <button @click="$router.back()" class="mb-2">← Volver</button>
    <h2>Producto: {{ barcode }}</h2>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="error" class="text-red-500">{{ error }}</div>
    <div v-else-if="product">
      <h3>{{ product.name }}</h3>
      <p>Marca: {{ product.brand }}</p>
      <p>Categoría: {{ product.category }}</p>
      <p>Precio: {{ product.price ?? 'N/D' }}</p>
      <div v-if="score">
        <h4>Scoring</h4>
        <p>Económico: {{ score.econ }}</p>
        <p>Ambiental: {{ score.env }}</p>
        <p>Social: {{ score.soc }}</p>
        <p><strong>Overall: {{ score.overall }}</strong></p>
      </div>
      <button @click="addToList" class="mt-2 bg-green-600 text-white px-3 py-1">Agregar a lista</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getProduct, scoreProduct } from '@/services/api'
import { useShoppingList } from '@/store/useShoppingList'

const route = useRoute()
const barcode = route.params.barcode as string
const loading = ref(true)
const error = ref('')
const product = ref<any>(null)
const score = ref<any>(null)
const store = useShoppingList()

onMounted(async () => {
  try {
    product.value = await getProduct(barcode)
    score.value = await scoreProduct(barcode)
  } catch (e: any) {
    error.value = e.message || JSON.stringify(e)
  } finally {
    loading.value = false
  }
})

function addToList(){
  store.add(barcode)
  alert('Agregado a la lista')
}
</script>
