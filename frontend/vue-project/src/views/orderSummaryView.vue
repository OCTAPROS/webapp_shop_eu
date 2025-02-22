<template>
  <v-container>
    <h2 class="text-h4  mb-6 bg-green-lighten-1 pa-4">Gratulacje!</h2>
    <v-row>
      <v-col cols="12" md="12">
        <v-card>
          <v-card-title class="ml-3">Twoje zamówienie zostało przesłane</v-card-title>
          <v-card-text>
            <v-list>
              <v-list-item>
                <v-list-item-title>
                  Status zamówienia to: {{ orderResponse?.status }}
                </v-list-item-title>
              </v-list-item>
              <v-list-item>
                <v-list-item-title>
                  Data złożenia zamówienia: {{ orderResponse?.date }}
                </v-list-item-title>
              </v-list-item>
            </v-list>            
          </v-card-text>
        </v-card>
      </v-col>

      <v-btn class="my-6" color="primary" block @click="back()">
        Powrót do strony głównej
      </v-btn>
    </v-row>
  </v-container>


</template>

<script setup lang="ts">
import { computed } from "vue";
import { useCustomerStore } from '../stores/customerStore';
import { useRouter } from 'vue-router'


const customerStore = useCustomerStore();
const router = useRouter()
const orderResponse = computed(() => customerStore.orderResponse);


const back = () => {
  router.push('/')
}


</script>

