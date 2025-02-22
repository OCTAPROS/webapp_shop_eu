<template>
  <v-container>
    <h2 class="text-h4 font-weight-bold mb-6 text-center">Statystyki sklepu</h2>

    <v-row>
      <!-- Sprzedaż miesięczna (Liniowy) -->
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="text-h5 mb-3">Sprzedaż miesięczna</h3>
          <LineChart :chart-data="salesData" :chart-options="chartOptions" />
        </v-card>
      </v-col>

      <!-- Kategorie najczęściej kupowane (Kołowy) -->
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="text-h5 mb-3">Najczęściej kupowane kategorie</h3>
          <PieChart :chart-data="categoryData" :chart-options="chartOptions" />
        </v-card>
      </v-col>

      <!-- Przychody miesięczne (Słupkowy) -->
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="text-h5 mb-3">Porównanie przychodów</h3>
          <BarChart :chart-data="revenueData" :chart-options="chartOptions" />
        </v-card>
      </v-col>

      <!-- Liczba nowych użytkowników (Obszarowy) -->
      <v-col cols="12" md="6">
        <v-card class="pa-4">
          <h3 class="text-h5 mb-3">Liczba nowych użytkowników</h3>
          <LineChart :chart-data="usersData" :chart-options="chartOptions" />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { LineChart, PieChart, BarChart } from 'vue-chart-3';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
    };

    const salesData = ref({
      labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj'],
      datasets: [
        {
          label: 'Sprzedaż',
          data: [120, 150, 180, 220, 300],
          borderColor: '#3f51b5',
          backgroundColor: 'rgba(63, 81, 181, 0.2)',
        },
      ],
    });

    const categoryData = ref({
      labels: ['Elektronika', 'Odzież', 'Kosmetyki', 'Książki'],
      datasets: [
        {
          label: 'Liczba zakupów',
          data: [40, 30, 20, 10],
          backgroundColor: ['#ff9800', '#4caf50', '#2196f3', '#e91e63'],
        },
      ],
    });

    const revenueData = ref({
      labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj'],
      datasets: [
        {
          label: 'Przychód (zł)',
          data: [5000, 7000, 8000, 11000, 13000],
          backgroundColor: '#4caf50',
        },
      ],
    });

    const usersData = ref({
      labels: ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj'],
      datasets: [
        {
          label: 'Nowi użytkownicy',
          data: [50, 75, 120, 160, 200],
          borderColor: '#e91e63',
          backgroundColor: 'rgba(233, 30, 99, 0.2)',
        },
      ],
    })
</script>