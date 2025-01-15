<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <main>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Sklep Online</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/">Strona główna</v-btn>
      <v-btn to="/products">Produkty</v-btn>
      <v-btn to="/cart">Koszyk</v-btn>
    </v-app-bar>
    <div>
      <router-view></router-view>
    </div>

  </main>
</template>