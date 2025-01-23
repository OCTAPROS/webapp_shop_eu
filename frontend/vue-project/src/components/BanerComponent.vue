<template>
<v-container class="mt-12">
  <v-sheet
    class="banner rounded-xl"
    height="400px"
    style="background-image: url('https://placehold.co/1920x600'); background-size: cover; background-position: center;"
  >
    <v-container class="fill-height d-flex flex-column justify-center align-center text-center white--text">
      <h1 class="text-h2 font-weight-bold">Witamy w naszym sklepie!</h1>
      <p class="text-h5 mt-3">Najlepsze produkty w jednym miejscu.</p>
      <v-btn class="mt-5" color="primary" large to="/products">
        Przeglądaj produkty
      </v-btn>
    </v-container>
  </v-sheet>
</v-container>
</template>