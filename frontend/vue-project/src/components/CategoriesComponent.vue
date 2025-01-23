<template>
    <v-container class="my-10">
      <h2 class="text-h4 font-weight-bold mb-6 text-center">
        Kategorie produktów
      </h2>
      <v-row>
        <v-col
          v-for="category in categories"
          :key="category.name"
          cols="12"
          sm="6"
          lg="3"
        >
          <v-card
            class="hoverable"
            height="200px"
            style="background-image: url('https://placehold.co/400x300'); background-size: cover; background-position: center;"
          >
            <v-card-title class="text-h6 white--text text-uppercase">
              {{ category.name }}
            </v-card-title>
            <v-card-actions>
              <v-btn text color="primary" to="/products">Zobacz więcej</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
</template>
<script setup lang="ts">
const categories = [
        {
          name: "Elektronika",
          image: "https://placehold.co/400x300",
        },
        {
          name: "Moda",
          image: "https://placehold.co/400x300",
        },
        {
          name: "Dom i ogród",
          image: "https://placehold.co/400x300",
        },
        {
          name: "Sport i turystyka",
          image: "https://placehold.co/400x300",
        },
      ]
</script>