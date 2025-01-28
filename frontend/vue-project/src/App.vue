<template>
  <v-app>
    <TopBarComponent :quantity="quant" />
    <v-main>
     

      <router-view />


    <FotterComponent />
  </v-main>
  </v-app>
</template>

<script setup>
import { computed } from 'vue';
import TopBarComponent from './components/TopBarComponent.vue';
import FotterComponent from './components/FotterComponent.vue';
import { useCartStore } from '@/stores/cart';

const cartStore = useCartStore();

const quant = computed(()=>cartStore.totalItems)

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
