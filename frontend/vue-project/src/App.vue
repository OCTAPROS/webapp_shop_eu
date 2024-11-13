<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<v-app>
  <v-app-bar app color="primary" dark>
    <v-toolbar-title>Sklep Online</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn to="/">Strona główna</v-btn>
    <v-btn to="/products">Produkty</v-btn>
    <v-btn to="/cart">Koszyk</v-btn>
  </v-app-bar>

  <v-main>
    <router-view></router-view>
  </v-main>

  <v-footer app color="grey lighten-4">
    <v-col class="text-center">aaa</v-col>
  </v-footer>
</v-app>
</template>

<style scoped>
.text {
  font-size: large;
}
</style>
