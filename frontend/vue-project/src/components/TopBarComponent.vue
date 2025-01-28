<template>
<v-app-bar app>
  <v-container>
    <v-row align="center" justify="space-between">
      <v-col cols="auto">
        <RouterLink to="/" class="home">
          <h1 class="text-h5 font-weight-bold mb-0 home" >Mój Sklep</h1>
        </RouterLink>
      </v-col>
      <v-col cols="auto">
        <v-btn text to="/products">Produkty</v-btn>
        <v-btn text to="/login">Login</v-btn>
        <v-btn text to="/cart" >Koszyk ({{ props.quantity }})</v-btn>
      </v-col>
    </v-row>
  </v-container>
</v-app-bar>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  quantity: Number

})

// const cartStore = useCartStore();

// onMounted(() => {
//   const cartQuantity = computed(() => cartStore.totalItems)
// })

</script>
<style>
.home{
  text-decoration: none;
  color: rgb(37, 116, 243);
}
  </style>