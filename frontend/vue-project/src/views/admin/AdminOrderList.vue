<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Zamówienia</h2>

    <!-- <v-btn color="primary" class="mb-4" @click="openDialog(defaultProduct)">Dodaj produkt</v-btn> -->

    <v-data-table
      :headers="headers"
      :items="orders"
      item-key="title"
      items-per-page="25"
      :sort-by="[{ key: 'id', order: 'desc' }]"
      >
    </v-data-table>

    <!-- <ProductDialog ref="productDialog" @save="saveProduct" /> -->
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { OrderService } from '@/api/orderService';
import { useOrderStore } from '@/stores/orderAdminStore'

const orderService = new OrderService();
const orderStore = useOrderStore()

const headers = [
        { title: 'id', value: 'id' },
        { title: 'customer_id', value: 'customer_id' },
        { title: 'first_name', value: 'first_name' },
        { title: 'last_name', value: 'last_name' },
        { title: 'order_number', value: 'order_number' },
        { title: 'order_status', value: 'order_status' },
        { title: 'payment_method', value: 'payment_method' },
        { title: 'payment_method_id', value: 'payment_method_id' },
        { title: 'delivery_method', value: 'delivery_method' },
        { title: 'delivery_method_id', value: 'delivery_method_id' },
        { title: 'phone_number', value: 'phone_number' },
        { title: 'city', value: 'city' },
        { title: 'street', value: 'street' },
      ]

const orders = computed(()=> orderStore.availableOrders) 


onMounted(() => {
  orderStore.fetchCustomers(3000, 12000)
  
});

</script>
