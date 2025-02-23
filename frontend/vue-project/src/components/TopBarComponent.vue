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
          <v-btn text="true" to="/products">Produkty</v-btn>
          <v-btn text="true" to="/cart" >Koszyk ({{ props.quantity }})</v-btn>
          <v-btn v-if="!props.isLogged" text="true" to="/login">Login</v-btn>
          <v-btn v-if="props.isLogged" text="true" to="/admin/products" >Panel Administracyjny </v-btn>
          <span v-if="props.isLogged">{{  props.userEmail }}</span>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink } from 'vue-router';

const props = defineProps({
  quantity: Number,
  isLogged: Boolean,
  userEmail: String,

})

</script>
<style>
.home{
  text-decoration: none;
  color: rgb(37, 116, 243);
}
</style>
