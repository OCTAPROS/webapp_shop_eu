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

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
      <v-otp-input></v-otp-input>
      <v-date-picker></v-date-picker>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.text {
  font-size: large;
}
</style>
