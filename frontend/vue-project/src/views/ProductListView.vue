<script setup lang="ts">
import ProductList from '@/components/ProductList.vue';
const products = [
        {
          id: 1,
          name: 'Produkt A',
          price: 199.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu A',
        },
        {
          id: 2,
          name: 'Produkt B',
          price: 249.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu B',
        },
        {
          id: 3,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu C',
        },
        {
          id: 4,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu C',
        },
        {
          id: 5,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu C',
        },
        {
          id: 6,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu C',
        },
        {
          id: 7,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
          description: 'Opis produktu C',
        },
        {
          id: 8,
          name: 'Produkt C',
          price: 299.99,
          image: 'https://fakeimg.pl/150x100/9babf2/081478?font=museo',
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