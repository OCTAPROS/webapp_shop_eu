<template>
  <v-container>
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

      <v-btn color="primary" type="submit">Login</v-btn>
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
        const response = await axios.post('http://localhost:8001/login', {
          email: this.email,
          password: this.password,
        });
        const token = response.data.token;
        localStorage.setItem('jwt', token);
        console('Login successful!');
      } catch (error) {
        console.error(error);
        alert('Login failed. Please try again.');
      }
    },
  },
};
</script>
