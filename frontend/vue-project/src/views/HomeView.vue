<!-- <script setup lang="ts">
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
</template> -->




<template>
  <v-container>
    <v-row>
      <!-- Filtry (lewa kolumna) -->
      <v-col cols="12" md="3">
        <v-card class="pa-4">
          <h3 class="text-h6 mb-4">Filtry</h3>

          <!-- Filtr kategorii -->
          <v-select
            v-model="filters.category"
            :items="categories"
            label="Kategoria"
            outlined
            dense
          />

          <!-- Filtr zakresu cen -->
          <h4 class="text-subtitle-1 mt-6">Zakres cen</h4>
          <v-range-slider
            v-model="filters.priceRange"
            :min="minPrice"
            :max="maxPrice"
            :tick-size="5"
            hide-details
            label="Zakres"
          >
            <template #prepend>
              <span>{{ filters.priceRange[0] }} zł</span>
            </template>
            <template #append>
              <span>{{ filters.priceRange[1] }} zł</span>
            </template>
          </v-range-slider>

          <v-btn
            class="mt-6"
            color="primary"
            block
            @click="applyFilters"
          >
            Zastosuj filtry
          </v-btn>
        </v-card>
      </v-col>

      <!-- Lista produktów (prawa kolumna) -->
      <v-col cols="12" md="9">
        <v-row>
          <v-col
            v-for="product in paginatedProducts"
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
                <v-btn color="primary" text>Dodaj do koszyka</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>

        <!-- Paginacja -->
        <v-pagination
          v-model="currentPage"
          :length="pageCount"
          class="mt-4"
          color="primary"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      // Lista produktów
      products: [
        { id: 1, name: "Produkt 1", category: "Kategoria 1", price: 50, image: "https://placehold.co/400x300" },
        { id: 2, name: "Produkt 2", category: "Kategoria 2", price: 120, image: "https://placehold.co/400x300" },
        { id: 3, name: "Produkt 3", category: "Kategoria 1", price: 200, image: "https://placehold.co/400x300" },
        { id: 4, name: "Produkt 4", category: "Kategoria 3", price: 300, image: "https://placehold.co/400x300" },
        { id: 5, name: "Produkt 5", category: "Kategoria 2", price: 80, image: "https://placehold.co/400x300" },
        // Dodaj więcej produktów, aby przetestować paginację
      ],
      // Filtry
      filters: {
        category: null,
        priceRange: [0, 500],
      },
      categories: ["Kategoria 1", "Kategoria 2", "Kategoria 3"],
      minPrice: 0,
      maxPrice: 500,
      // Paginacja
      currentPage: 1,
      itemsPerPage: 6,
    };
  },
  computed: {
    // Filtrowane produkty
    filteredProducts() {
      return this.products.filter((product) => {
        const inCategory =
          !this.filters.category || product.category === this.filters.category;
        const inPriceRange =
          product.price >= this.filters.priceRange[0] &&
          product.price <= this.filters.priceRange[1];
        return inCategory && inPriceRange;
      });
    },
    // Produkty na aktualnej stronie
    paginatedProducts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.filteredProducts.slice(start, end);
    },
    // Liczba stron
    pageCount() {
      return Math.ceil(this.filteredProducts.length / this.itemsPerPage);
    },
  },
  methods: {
    applyFilters() {
      this.currentPage = 1; // Resetuj paginację po zastosowaniu filtrów
    },
  },
};
</script>

<style scoped>
.text-gray {
  color: #6c757d;
}
</style>
