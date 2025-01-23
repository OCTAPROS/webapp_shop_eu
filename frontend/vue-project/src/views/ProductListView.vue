
<template>
  <v-container class="mt-12">
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
          <router-link :to="`/product/${product.id}`" class="product-link">
            <v-card class="product-link" >
              <v-img
                :src="'https://placehold.co/400x300'"
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
          </router-link>
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

<script setup lang="ts">
import { defineComponent, onMounted, ref } from 'vue';
import { useProductStore } from '@/stores/productStore';
import { RouterLink, RouterView } from 'vue-router';

const productStore = useProductStore();

const isLoading = productStore.isLoading
const error = productStore.error
const products = computed(()=> productStore.availableProducts) 

onMounted(() => {
  productStore.fetchProducts();
});

// Lista produktów
// products: [
//   { id: 1, name: "Produkt 1", category: "Kategoria 1", price: 50, image: "https://placehold.co/400x300" },
//   { id: 2, name: "Produkt 2", category: "Kategoria 2", price: 120, image: "https://placehold.co/400x300" },
//   { id: 3, name: "Produkt 3", category: "Kategoria 1", price: 200, image: "https://placehold.co/400x300" },
//   { id: 4, name: "Produkt 4", category: "Kategoria 3", price: 300, image: "https://placehold.co/400x300" },
//   { id: 5, name: "Produkt 5", category: "Kategoria 2", price: 80, image: "https://placehold.co/400x300" },
//   // Dodaj więcej produktów, aby przetestować paginację
// ],
// Filtry
const  filters = {
  category: null,
  priceRange: [0, 500],
}
const categories = ["Kategoria 1", "Kategoria 2", "Kategoria 3"]
const minPrice = 0
const maxPrice = 500
      // Paginacja
const currentPage = ref(1)
const itemsPerPage = 6


  // Filtrowane produkty
const filteredProducts = computed(() => {
  return products.value.filter((product: any) => {
    const inCategory =
      !filters.category || product.category === filters.category;
    const inPriceRange =
      product.price >= filters.priceRange[0] &&
      product.price <= filters.priceRange[1];
    return inCategory && inPriceRange;
  });
})
    // Produkty na aktualnej stronie
const paginatedProducts = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return filteredProducts.value.slice(start, end);
})
    // Liczba stron
const pageCount = computed(() => {
  return Math.ceil(filteredProducts.value.length / itemsPerPage);
})

const applyFilters = () => {
  currentPage.value = 1; 
}


</script>

<style scoped>
.text-gray {
  color: #6c757d;
}
.product-link {
  text-decoration: none;
  color: inherit;
}

/* Efekt wyróżnienia na hover */
.product-link:hover {
  transform: scale(1.02); /* Delikatne powiększenie */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Wyróżnienie */
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
</style>
