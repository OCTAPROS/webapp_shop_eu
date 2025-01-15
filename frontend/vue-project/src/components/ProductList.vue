<script>
export default {
  name: 'ProductList',
  props: {
    products: {
      type: Array,
      required: true,
    },
  },
  methods: {
    addToCart(product) {
      console.log(`Dodano produkt do koszyka: ${product.name}`);
    },
  },
  filters: {
    currency(value) {
      return new Intl.NumberFormat('pl-PL', {
        style: 'currency',
        currency: 'PLN',
      }).format(value);
    },
  },
};
</script>

<template>
  <v-container>
    <v-row>
      <v-col
        v-for="product in products"
        :key="product.id"
        cols="12"
        md="4"
      >
        <v-card>
          <v-img
            :src="product.image"
            :alt="product.name"
            height="200"
            class="align-center"
          ></v-img>
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.price | currency }}</v-card-subtitle>
          <v-card-text>{{ product.description }}</v-card-text>
          <v-card-actions>
            <v-btn @click="addToCart(product)" color="primary">
              Dodaj do koszyka
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
</style>