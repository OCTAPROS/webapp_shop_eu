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
  </v-container>
</template>

<script>
import axios from '@/plugins/axios';

export default {
  data() {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8001/auth/token', {
          username: this.email,
          password: this.password,
          grant_type: "",
          password:  "",
          scope: "",
          client_id: "",
          client_secret: "",
        });
        const token = response.data.access_token;
        localStorage.setItem('jwt', token);
        console.log('Login successful!');
      } catch (error) {
        console.error(error);
        console.log('Login failed. Please try again.');
      }
    },
  },
};
</script>

<style>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
  min-height: 60vh;
}

</style>