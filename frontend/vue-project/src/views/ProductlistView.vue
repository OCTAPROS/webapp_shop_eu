<script setup lang="ts">
import ProductList from '@/components/ProductList.vue';
const products = [
        {
          id: 1,
          nazwa: 'Produkt A',
          cena: 199.99,
          zdjecie: 'https://via.placeholder.com/150',
          opis: 'Opis produktu A',
        },
        {
          id: 2,
          name: 'Produkt B',
          price: 249.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu B',
        },
        {
          id: 3,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
        {
          id: 4,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
        {
          id: 5,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
        {
          id: 6,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
        {
          id: 7,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
        {
          id: 8,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://via.placeholder.com/150',
          description: 'Opis produktu C',
        },
      ]
</script>

<template>
  <div class="about">
    <ProductList :products="products" />
  </div>
</template>

<style>

</style>
