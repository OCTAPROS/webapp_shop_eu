<template>
  <v-container>
    <!-- Główna sekcja -->
    <v-row class="my-4" align="center" justify="center">
      <!-- Obraz produktu -->
      <v-col cols="12" md="6">
        <v-img
          :src="product.image"
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
        <p>{{ product.longDescription }}</p>
      </v-col>
    </v-row>

    <!-- Sugerowane produkty -->
    <v-row class="my-8">
      <v-col cols="12">
        <h2 class="text-h5 mb-4">Sugerowane produkty</h2>
      </v-col>
      <v-col
        v-for="suggested in suggestedProducts"
        :key="suggested.id"
        cols="12"
        md="4"
      >
        <v-card>
          <v-img
            :src="suggested.image"
            :alt="suggested.name"
            aspect-ratio="1.5"
          />
          <v-card-title>{{ suggested.name }}</v-card-title>
          <v-card-subtitle>{{ suggested.price }} zł</v-card-subtitle>
          <v-card-actions>
            <v-btn color="primary" text>Wyświetl</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      quantity: 1,
      product: {
        id: 1,
        name: "Przykładowy produkt",
        shortDescription: "Krótki opis produktu",
        longDescription: "Tutaj znajduje się szczegółowy opis produktu.",
        price: 99.99,
        image: "https://placehold.co/400x400",
      },
      suggestedProducts: [
        {
          id: 2,
          name: "Produkt 2",
          price: 49.99,
          image: "https://placehold.co/400x300",
        },
        {
          id: 3,
          name: "Produkt 3",
          price: 79.99,
          image: "https://placehold.co/400x300",
        },
        {
          id: 4,
          name: "Produkt 4",
          price: 129.99,
          image: "https://placehold.co/400x300",
        },
      ],
    };
  },
  methods: {
    increaseQuantity() {
      this.quantity = Math.min(this.quantity + 1, 99); // Maksymalna ilość 99
    },
    decreaseQuantity() {
      this.quantity = Math.max(this.quantity - 1, 1); // Minimalna ilość 1
    },
    addToCart() {
      console.log(`Dodano ${this.quantity} szt. produktu do koszyka`);
      // Tutaj możesz obsłużyć logikę dodawania do koszyka
    },
  },
};
</script>

<style scoped>
.text-gray {
  color: #6c757d;
}
</style>
