<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6">Twój koszyk</h2>

    <v-row>
      <v-col cols="12" md="8">
        <v-card
          v-for="item in cart"
          :key="item.id"
          class="mb-4"
        >
          <v-card-title>
            <v-img
              :src="'https://placehold.co/400x400'"
              :alt="item.name"
              class="mr-4"
              max-width="100"
              aspect-ratio="1"
            />
            <div>
              <h3 class="text-h6 mb-2">{{ item.name }}</h3>
              <p>{{ item.price }} zł</p>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn icon @click="updateQuantity(item.id, item.quantity - 1)">
              <v-icon>mdi-minus</v-icon>
            </v-btn>
            <span>{{ item.quantity }}</span>
            <v-btn icon @click="updateQuantity(item.id, item.quantity + 1)">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn color="error" text @click="removeFromCart(item.id)">
              Usuń
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="12" md="4">
        <v-card>
          <v-card-title>Podsumowanie</v-card-title>
          <v-card-text>
            <p>Razem: {{ totalPrice.toFixed(2) }} zł</p>
            <p>Produkty: {{ totalItems }}</p>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" block>
              Przejdź do płatności
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useCartStore } from '../stores/cart';

const cartStore = useCartStore();

const cart = computed(() => cartStore.cart); 
const totalPrice = computed(() => cartStore.totalPrice);
const totalItems = computed(() => cartStore.totalItems);

const removeFromCart = (id: number) => {
  cartStore.removeFromCart(id);
};

const updateQuantity = (id: number, quantity: number) => {
  cartStore.updateQuantity(id, quantity);
};

</script>