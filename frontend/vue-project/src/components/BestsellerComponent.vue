<template>
  <v-container class="my-10">
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Bestsellery</h2>
    <v-row>
      <v-col
        v-for="product in bestsellers"
        :key="product.id"
        cols="12"
        sm="6"
        lg="4"
      >
        <v-card>
          <v-img
            :src="product.image"
            :alt="product.name"
            class="rounded"
            aspect-ratio="1.5"
          />
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.price }} zł</v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" text >Dodaj do koszyka</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup lang="ts">

const bestsellers = [
        {
          id: 1,
          name: "Produkt 1",
          price: 99.99,
          image: "https://placehold.co/400x300",
        },
        {
          id: 2,
          name: "Produkt 2",
          price: 149.99,
          image: "https://placehold.co/400x300",
        },
        {
          id: 3,
          name: "Produkt 3",
          price: 79.99,
          image: "https://placehold.co/400x300",
        },
      ]
</script>