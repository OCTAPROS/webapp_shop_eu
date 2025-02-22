<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Zarządzanie Klkientami</h2>

    <v-table>
      <thead>
        <tr>
          <th>Id</th>
          <th>Imie</th>
          <th>Nazwisko</th>
          <th>Akcje</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="product in customers" :key="product.id">
          <td>{{ product.id }}</td>
          <td>{{ product.name }}</td>
          <td>{{ product.last_name }}</td>
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
import { useCustomerStore } from '@/stores/customerStore';
import { ref } from 'vue';
import ProductDialog from '@/components/ProductDialog.vue';
import { Customer, defaultCustomer } from '@/models/Customer';


const customerStore = useCustomerStore();
const productDialog = ref(null);

const customers = computed(()=> customerStore.availableCustomers) 

const openDialog = (product?: Customer) => {
  productDialog?.value?.open(product);
};

const saveProduct = (product: Customer) => {
  if (product.id) {
  } else {
    // productStore.addProduct(product);
  }
};

const deleteProduct = (id: number) => {
  if (confirm("Czy na pewno chcesz usunąć ten produkt?")) {
  }
};

onMounted(() => {
  customerStore.fetchCustomers();
});

</script>
