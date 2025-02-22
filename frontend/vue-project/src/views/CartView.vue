<template>
  <v-container class="bg-grey-lighten-5">
    <h2 class="text-h4  mb-6 bg-blue-lighten-1 pa-4">Twój koszyk</h2>

    <v-row>
      <v-col cols="12" md="6">
        <v-card
          v-for="item in cart"
          :key="item.id"
          class="mb-4"
        >
          <v-card-title class="d-flex ">
            <v-img
              :src="'https://placehold.co/400x400'"
              :alt="item.name"
              class="mr-4"
              max-width="100"
              aspect-ratio="1"
            />
            <div>
              <h3 class="text-h6 mb-2">{{ item.name }}</h3>
              <p>cena: {{ item.price }} zł</p>
            </div>
          </v-card-title>
          <v-card-actions>
            <div>
              <div class="ml-4 mt-4">Ilość</div>
            <div>
            <v-btn icon @click="updateQuantity(item.id, item.quantity - 1)">
              <v-icon>mdi-minus</v-icon>
            </v-btn>
            <span>{{ item.quantity }}</span>
            <v-btn icon @click="updateQuantity(item.id, item.quantity + 1)">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </div>
        </div>
            <v-spacer></v-spacer>
            <v-btn color="error" text="true" @click="removeFromCart(item.id)">
              Usuń
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card>
          <v-card-title class="text-h4 mb-4">Podsumowanie</v-card-title>
          <v-card-text>
            <p class="text-h5">Produkty: {{ totalItems }}</p>
            <p class="text-h5">Razem: {{ totalPrice.toFixed(2) }} zł</p>
            <v-btn class="mt-8" block color="primary"  @click="goNext()">
              Przejdź dalej
            </v-btn>
          </v-card-text>
            
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useCartStore } from '../stores/cart';
import { useRouter } from 'vue-router'

const cartStore = useCartStore();
const router = useRouter()

const cart = computed(() => cartStore.cart); 
const totalPrice = computed(() => cartStore.totalPrice);
const totalItems = computed(() => cartStore.totalItems);

const removeFromCart = (id: number) => {
  cartStore.removeFromCart(id);
};

const updateQuantity = (id: number, quantity: number) => {
  cartStore.updateQuantity(id, quantity);
};

const goNext = () => {
  router.push('/checkout')
}


</script>