<template>
  <v-dialog v-model="dialog" max-width="500px">
    <v-card>
      <v-card-title>{{ editedProduct.id ? "Edytuj produkt" : "Dodaj produkt" }}</v-card-title>
      <v-card-text>
        <v-text-field label="Nazwa" :maxlength="50" v-model="editedProduct.name"></v-text-field>
        <v-select
          label="Marka"
          v-model="editedProduct.brand_id"
          :items="brands"
          item-title="dict_value"
          item-value="id"
        ></v-select>

        <!-- Lista rozwijalna dla typu -->
        <v-select
          label="Typ"
          v-model="editedProduct.product_type_id"
          :items="types"
          item-title="dict_value"
          item-value="id"
        ></v-select>
        <v-text-field label="Cena" type="number" v-model.number="editedProduct.price"></v-text-field>
        <v-text-field label="ean" type="sting" :maxlength="13" v-model="editedProduct.ean"></v-text-field>
        <v-text-field label="Stan na magazynie" type="number" v-model="editedProduct.qty_on_stock" min="0" step="1"></v-text-field>
        <v-textarea
          label="Opis"
          v-model="editedProduct.description"
          rows="3"
          auto-grow
           :maxlength="100"
        ></v-textarea>
      </v-card-text>
      <v-card-actions>
        <v-btn color="grey" @click="dialog = false">Anuluj</v-btn>
        <v-btn color="blue" @click="save" variant="flat">Zapisz</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import { Product, defaultProduct } from '@/models/Product';
import { Dict } from '@/models/Dict';
import { DictService } from '@/api/DictService';
import { useDictStore } from '@/stores/dictStore';

const emit = defineEmits(['save', 'open'])


const dictService = new DictService();
const dictStore = useDictStore();



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

const types = computed(() => dictStore.PRODUCT_TYPE)
const brands = computed(() => dictStore.BRAND)

onMounted(() => {
  dictStore.fetchBRAND()
  dictStore.fetchPRODUCT_TYPE()
})


defineExpose({ open });

</script>
