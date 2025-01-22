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
};
</script>

<template>
  <v-container class="">
    <v-row class="">
      <v-col v-for="product in products"
        :key="product.id"
        cols="12"
        md="4"
        no-gutters
        no-margin
        class="px-0 py-0 border-0"
      >
        <v-card class="border-0 rounded-b-0 rounded-t-0">
          <v-img v-if="product.image"
            :src="product.image"
            :alt="product.name"
            height="200"
            class="align-center"
          ></v-img>
          <div class="d-flex justify-center" v-else>
            <v-icon size="120px" icon="mdi-cube-off-outline" class="py-8"></v-icon>
          </div>
          
          <v-card-title>{{ product.name }}</v-card-title>
          <v-card-subtitle>{{ product.price.toFixed(2) }} PLN</v-card-subtitle>
          <v-card-text>{{ product.description }}</v-card-text>
          <v-card-actions>
            <v-btn @click="addToCart(product)" color="white" solid class="bg-primary">
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