<script setup lang="ts">
import { defineComponent, onMounted } from 'vue';
import { useProductStore } from '@/stores/productStore';
import { RouterLink, RouterView } from 'vue-router';
import ProductList from '@/components/ProductList.vue';

const productStore = useProductStore();

const isLoading = productStore.isLoading
const error = productStore.error
const products = computed(()=> productStore.availableProducts) 

onMounted(() => {
  productStore.fetchProducts();
});

</script>

<template>
  <v-layout class="rounded rounded-md">
    <v-app>
    <v-app-bar color="primary">
      <v-btn to="/"><v-icon icon="mdi-home"></v-icon></v-btn>
      <v-toolbar-title >Webstore</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn to="/account"><v-icon icon="mdi-account"></v-icon></v-btn>
      <v-btn to="/cart"><v-icon icon="mdi-cart"></v-icon></v-btn>

    </v-app-bar>
 
    <v-navigation-drawer>
      <v-list>
        <v-list-item title="Navigation drawer">tutaj będą filry i mmenu</v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="" style="min-height: 300px;">
      <div class="about">
        <ProductList v-if="products.length" :products="products" />
      </div>
    </v-main>
    
    <div>
      <router-view></router-view>
    </div>
  </v-app>
</v-layout>
</template>