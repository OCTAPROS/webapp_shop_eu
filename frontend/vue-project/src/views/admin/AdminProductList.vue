<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Zarządzanie produktami</h2>

    <v-btn color="primary" class="mb-4" @click="openDialog(defaultProduct)">Dodaj produkt</v-btn>

    <v-table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Nazwa</th>
          <th>Ilość na stanie</th>
          <th>Ean</th>
          <th>Cena</th>
          <th>Akcje</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in products" :key="product.id">
          <td>{{ product.id }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.qty_on_stock }}</td>
          <td>{{ product.ean }}</td>
          <td>{{ product.price }} zł</td>
          <td>
            <v-btn icon color="blue" @click="openDialog(product)">
              <v-icon>mdi-pencil</v-icon>
            </v-btn>
            <v-btn v-if="product.id" icon color="red" @click="deleteProduct(product.id)">
              <v-icon>mdi-delete</v-icon>
            </v-btn>
          </td>
        </tr>
      </tbody>
    </v-table>

    <ProductDialog ref="productDialog" @save="saveProduct" />
  </v-container>
</template>

<script setup lang="ts">
import { useProductStore } from '@/stores/productStore';
import { ref } from 'vue';
import ProductDialog from '@/components/ProductDialog.vue';
import { Product, defaultProduct } from '@/models/Product';


const productStore = useProductStore();
const productDialog = ref(null);

const products = computed(()=> productStore.availableProducts) 

const openDialog = (product?: Product) => {
  productDialog?.value?.open(product);
};

const saveProduct = (product: Product) => {
  if (product.id) {
    console.log('update', product)
    productStore.updateProduct(product);
  } else {
    console.log('add', product)
    // productStore.addProduct(product);
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
