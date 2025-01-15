<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<v-app>
  <v-main>
    <router-view></router-view>
  </v-main>
</v-app>

</template>

<style scoped>
.text {
  font-size: large;
}
</style>