<template>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title>{{ editedProduct.id ? "Edytuj produkt" : "Dodaj produkt" }}</v-card-title>
      <v-card-text>
        <v-text-field label="Nazwa" v-model="editedProduct.name"></v-text-field>
        <v-text-field label="marka" v-model="editedProduct.marka"></v-text-field>
        <v-text-field label="typ"  v-model="editedProduct.type"></v-text-field>
        <v-text-field label="Cena" type="number" v-model="editedProduct.price"></v-text-field>
        <v-text-field label="ean" type="number" v-model="editedProduct.ean"></v-text-field>
        <v-text-field label="Stan na magazynie" type="number" v-model="editedProduct.stock_count"></v-text-field>
        <v-text-field label="Opis" v-model="editedProduct.longDescription"></v-text-field>
        <v-text-field label="URL obrazu" v-model="editedProduct.image"></v-text-field>
      </v-card-text>
      <v-card-actions>
        <v-btn color="grey" @click="dialog = false">Anuluj</v-btn>
        <v-btn color="blue" @click="save" variant="flat">Zapisz</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Product, defaultProduct } from '@/models/Product';

const emit = defineEmits(['save', 'open'])

const dialog = ref(false);
const editedProduct = ref(new Product(defaultProduct));

const open = (product: Product) => {
  editedProduct.value = product ? { ...product } : new Product(defaultProduct);
  dialog.value = true;
  console.log('editedProduct.value', editedProduct.value)
};

const save = () => {
  emit('save', editedProduct.value);
  dialog.value = false;
};


defineExpose({ open });

</script>
