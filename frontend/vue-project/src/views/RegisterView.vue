<template>
  <v-container>
    <v-form @submit.prevent="register">
      <v-text-field
        label="Name"
        v-model="name"
        required
      ></v-text-field>

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

      <v-btn color="primary" type="submit">Register</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        const response = await axios.post('http://localhost:8001/register', {
          name: this.name,
          email: this.email,
          password: this.password,
        });
        alert('Registration successful!');
      } catch (error) {
        console.error(error);
        alert('Registration failed. Please try again.');
      }
    },
  },
};
</script>