<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="12">
        <v-card>
          <v-card-title class="ml-3">Posdumowanie</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item v-for="item in cart" :key="item.id">
                <v-list-item-title>
                  {{ item.name }} (x{{ item.quantity }})
                </v-list-item-title>
                <v-list-item-subtitle>{{ item.price }} zł</v-list-item-subtitle>
              </v-list-item>
            </v-list>
            <v-divider></v-divider>
            <p class="text-h5 ml-3 mt-6">Razem: <strong>{{ cartTotal }} zł</strong></p>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="12">
        <v-card>
          <v-card-title class="ml-3">Twoje dane</v-card-title>
          <v-card-text class="ml-3">
            <p><strong>Email:</strong> {{ user.email }}</p>
            <p><strong>Telefon:</strong> {{ user.id }}</p>
            <p><strong>Adres:</strong> {{ user.is_active }}</p>
            <p><strong>Adres:</strong> {{ user.is_superuser }}</p>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Metody płatności</v-card-title>
          <v-card-text>
            <v-radio-group v-model="selectedPayment">
              <v-radio
                v-for="method in paymentMethods"
                :key="method.id"
                :label="method.dict_value"
                :value="method.id"
              ></v-radio>
            </v-radio-group>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card>
          <v-card-title>Metody dostawy</v-card-title>
          <v-card-text>
            <v-radio-group v-model="selectedDelivery">
              <v-radio
                v-for="method in deliveryMethods"
                :key="method.id"
                :label="method.dict_value"
                :value="method.id"
              ></v-radio>
            </v-radio-group>
          </v-card-text>
        </v-card>
      </v-col>

      <v-btn class="my-6" color="primary" block @click="order()">
        Wyślij
      </v-btn>
    </v-row>
  </v-container>
 
  <!-- przycisk płatność -> strzał do api, w którym wysyłam to wszystko
  result to wraca id_zamówienia i delivery date -->


</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useCartStore } from '../stores/cart';
import { useCustomerStore } from '../stores/customerStore';
import { DictService } from '@/api/DictService';
import { useDictStore } from '@/stores/dictStore';
import { Order } from '@/models/Order'
import { useRouter } from 'vue-router'

const cartStore = useCartStore();
const userStore = useCustomerStore();
const dictService = new DictService();
const dictStore = useDictStore();

const user = computed(() => userStore.user);
const router = useRouter()

// LISTA METOD PŁATNOŚCI

const selectedPayment = ref("blik");
const selectedDelivery = ref("selectedDelivery");

const paymentMethods = computed(() => dictStore.availablePAYMENT_METHOD)
const deliveryMethods = computed(() => dictStore.availableDELIVERY_METHOD)

const order = () => {
  const ord = new Order({
    customer_id: user.value.customer_id,
    payment_method_id: selectedPayment.value,
    delivery_method_id: selectedDelivery.value,
    order_rows: orderRows.value,
  })
  userStore.order(ord)
  cartStore.clearCart()
  router.push('/orderSummary')
  
}

const orderRows = computed(() => cartStore.orderRows)
const cart = computed(() => cartStore.cart); 


// SUMA KOSZYKA
const cartTotal = computed(() =>
  cartStore.cart.reduce((sum, item) => sum + item.price * item.quantity, 0)
);

onMounted(() => {
  userStore.fetchUser()
  dictStore.fetchPAYMENT_METHOD()
  dictStore.fetchDELIVERY_METHOD()
})
</script>

