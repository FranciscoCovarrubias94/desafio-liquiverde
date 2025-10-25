<template>
  <div>
    <h2 class="text-h5 mb-4">Escáner de Producto</h2>

    <v-text-field
      v-model="barcode"
      label="Código de barras"
      prepend-inner-icon="mdi-barcode"
      class="mb-2"
    />

    <v-btn color="primary" @click="fetchProduct">Buscar</v-btn>

    <div v-if="product" class="mt-4">
      <v-card>
        <v-img :src="product.image_url" height="120" cover />
        <v-card-title>{{ product.name }}</v-card-title>
        <v-card-subtitle>{{ product.brand }}</v-card-subtitle>
        <v-card-actions>
          <v-btn color="secondary" @click="addToList(product)">
            Agregar a lista
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>

    <div v-if="list.length" class="mt-6">
      <h3 class="text-h6 mb-2">Lista actual</h3>
      <v-list>
        <v-list-item
          v-for="(item, index) in list"
          :key="index"
          :title="item.name"
          :subtitle="item.brand"
        />
      </v-list>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getProduct } from '@/services/api'

const barcode = ref('')
const product = ref<any>(null)
const list = ref<any[]>([])

async function fetchProduct() {
  product.value = await getProduct(barcode.value)
}

function addToList(prod: any) {
  const stored = JSON.parse(localStorage.getItem('product_list') || '[]')
  if (!stored.find((p: any) => p.barcode === prod.barcode)) {
    stored.push(prod)
    localStorage.setItem('product_list', JSON.stringify(stored))
    list.value = stored
  }
}


onMounted(() => {
  const stored = localStorage.getItem('product_list')
  if (stored) {
    list.value = JSON.parse(stored)
  }
})
</script>
