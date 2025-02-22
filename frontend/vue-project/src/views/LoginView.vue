<template>
  <v-container  class="login-container">
    <v-form @submit.prevent="login">
      <v-text-field
        label="Email"
        v-model="email"
        type="email"
        required
      ></v-text-field>

      <v-text-field
        label="Password"
        v-model="password"
        type="password"
        required
      ></v-text-field>

      <div class="d-flex flex-column gap-4">
        <v-btn color="primary" type="submit" class="my-2">Login</v-btn>
        <router-link to="/register" class="mt-2">Rejestracja</router-link>
      </div>
    </v-form>
boczek@gmail.com
 Pass123!
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from '@/plugins/axios';
import { useRouter } from 'vue-router'
import { useCustomerStore } from '../stores/customerStore';

const customerStore = useCustomerStore()

const router = useRouter()

const email = ref('')
const password = ref('')


const login = async () => {
 try {
    const response = await axios.post('http://localhost:8001/auth/token', {
      username: email.value,
      password: password.value,
    });
    const token = response.data.access_token;
    localStorage.setItem('jwt', token);
    customerStore.fetchUser()
    router.push('/')
  } catch (error) {
    console.error(error);
  }
}

</script>

<style>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
  min-height: 60vh;
}

</style>