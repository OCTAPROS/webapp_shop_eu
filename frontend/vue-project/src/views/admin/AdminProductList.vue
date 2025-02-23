<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Zarządzanie produktami</h2>

    <v-btn color="primary" class="mb-4" @click="openDialog(defaultProduct)">Dodaj produkt</v-btn>

    <v-data-table
      :headers="headers"
      :items="products"
      item-key="name"
      items-per-page="25"
      :sort-by="[{ key: 'id', order: 'desc' }]"
      >
      <template v-slot:item.actions="{ item }">
        <v-btn icon color="blue" @click="openDialog(item)">
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
        <v-btn v-if="item.id" icon color="red" @click="deleteProduct(item.id)">
          <v-icon>mdi-delete</v-icon>
        </v-btn>
      </template>
      <template v-slot:no-data>
        <v-btn
          color="primary"
          @click="productStore.fetchProducts()"
        >
        Reset
      </v-btn>
    </template>
    </v-data-table>

    <ProductDialog ref="productDialog" @save="saveProduct" />
  </v-container>
</template>

<script setup lang="ts">
import { useProductStore } from '@/stores/productStore';
import { ref } from 'vue';
import ProductDialog from '@/components/ProductDialog.vue';
import { Product, defaultProduct } from '@/models/Product';

const headers = [
        { title: 'Id', value: 'id' },
        { title: 'Nazwa', value: 'name' },
        { title: 'Ilość na stanie', value: 'qty_on_stock' },
        { title: 'Ean', value: 'ean' },
        { title: 'Cena', value: 'price' },
        { title: 'Akcje', value: 'actions' }
      ]

const productStore = useProductStore();
const productDialog = ref(null);

const products = computed(()=> productStore.availableProducts) 

const openDialog = (product?: Product) => {
  productDialog?.value?.open(product);
};

const saveProduct = (product: Product) => {
  if (product.id) {
    productStore.updateProduct(product);
  } else {
    productStore.addProduct(product);
  }
};

const deleteProduct = (id: number) => {
  if (confirm("Czy na pewno chcesz usunąć ten produkt?")) {
    productStore.deleteProduct(id);
  }
};

onMounted(() => {
  productStore.fetchProducts();
});

</script>
