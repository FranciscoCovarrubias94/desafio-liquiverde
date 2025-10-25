import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useShoppingList = defineStore('shoppingList', () => {
  const items = ref<Array<{barcode: string, qty: number}>>([])

  function add(barcode: string, qty=1){
    const found = items.value.find(i => i.barcode === barcode)
    if(found) found.qty += qty
    else items.value.push({barcode, qty})
  }

  function remove(barcode: string){
    items.value = items.value.filter(i => i.barcode !== barcode)
  }

  function clear(){
    items.value = []
  }

  return { items, add, remove, clear }
})
