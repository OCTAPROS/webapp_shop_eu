<template>
  <v-container>
    <!-- Główna sekcja -->
    <v-row class="my-4" align="center" justify="center">
      <!-- Obraz produktu -->
      <v-col cols="12" md="6">
        <v-img
          :src="'https://placehold.co/400x400'"
          :alt="product.name"
          class="rounded"
          aspect-ratio="1"
        />
      </v-col>

      <!-- Szczegóły produktu -->
      <v-col cols="12" md="6">
        <h1 class="text-h4">{{ product.name }}</h1>
        <p class="text-subtitle-1 text-gray">{{ product.shortDescription }}</p>
        <p class="text-h5 font-weight-bold mt-4">{{ product.price }} zł</p>
        <v-divider class="my-4" />

        <!-- Input zmiany ilości produktów -->
        <div class="d-flex align-center mb-4">
          <v-btn
            variant="outlined"
            color="primary"
            icon
            @click="decreaseQuantity"
          >
            <v-icon>mdi-minus</v-icon>
          </v-btn>

          <v-text-field
            v-model="quantity"
            type="number"
            class="mx-3"
            style="max-width: 80px"
            min="1"
            max="99"
            outlined
          />

          <v-btn
            variant="outlined"
            color="primary"
            icon
            @click="increaseQuantity"
          >
            <v-icon>mdi-plus</v-icon>
          </v-btn>
          <v-btn class="ml-5" color="primary" @click="addToCart">
            Dodaj do koszyka
          </v-btn>
        </div>
      </v-col>
    </v-row>

    <!-- Opis szczegółowy -->
    <v-row class="my-8">
      <v-col cols="12">
        <h2 class="text-h5 mb-4">Opis produktu</h2>
        <p>{{ product?.longDescription || lorem }}</p>
      </v-col>
    </v-row>
    
    <!-- Sugerowane produkty -->
    <BestsellerComponent />
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useProductStore } from '@/stores/productStore';
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import BestsellerComponent from '@/components/BestsellerComponent.vue';

const productStore = useProductStore();
const route = useRoute(); 

const productId = computed(() => Number(route.params.id));

const product = computed(() =>
  productStore.availableProducts.find((item: any) => item.id === productId.value)
);

const quantity = ref(1)

const lorem = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Non consequatur in rerum labore voluptatum dolorum ullam a aliquam voluptatibus ipsum debitis, laudantium fugit excepturi? Voluptatum, ipsa! Iure libero saepe exercitationem, reiciendis debitis quis adipisci corrupti id dicta placeat vitae dolore beatae! Asperiores amet in ex atque, illum soluta aliquid quos!'

function increaseQuantity() {
  quantity.value = Math.min(quantity.value + 1, 99);
}
function decreaseQuantity() {
  quantity.value = Math.max(quantity.value - 1, 1);
}
function addToCart() {
  console.log(`Dodano ${quantity.value} szt. produktu do koszyka`);
}


</script>

<style scoped>
.text-gray {
  color: #6c757d;
}
</style>
