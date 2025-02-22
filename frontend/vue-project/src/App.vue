<template>
  <v-app>
    <TopBarComponent :quantity="quant" :isLogged="isLoged" :userEmail="userEmail" />
    <v-main>
     

      <router-view />


    <!-- <FotterComponent /> -->
  </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import TopBarComponent from '@/components/TopBarComponent.vue';
// import FotterComponent from './components/FotterComponent.vue';
import { useCartStore } from '@/stores/cart';
import { useCustomerStore } from '@/stores/customerStore'

const customerStore = useCustomerStore();
const cartStore = useCartStore();

const quant = computed(()=>cartStore.totalItems)

const isLoged = computed(() => !!customerStore.user.email)
const userEmail = computed(() => customerStore?.user?.email)

</script>

<style scoped>
.banner {
  position: relative;
  overflow: hidden;
}
.text-center {
  text-align: center;
}
.text-md-end {
  text-align: right;
}
</style>
