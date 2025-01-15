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

      <div class="flex-column">
        <v-btn color="primary" type="submit">Login</v-btn>
        <v-btn color="secondary" @click="goToRegister">Rejestracja</v-btn>
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
        });
        const token = response.data.access_token;
        localStorage.setItem('jwt', token);
        console.log('Login successful!');
      } catch (error) {
        console.error(error);
        console.log('Login failed. Please try again.');
      }
    },
    goToRegister() {
      this.$router.push('/register');
    },
  },
};
</script>

<style>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  text-align: center;
}

</style>