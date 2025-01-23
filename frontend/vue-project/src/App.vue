<template>
  <v-app>
    <TopBarComponent />
    <v-main>
     

      <router-view />


    <FotterComponent />
  </v-main>
  </v-app>
</template>

<script>
import TopBarComponent from './components/TopBarComponent.vue';
import FotterComponent from './components/FotterComponent.vue';


export default {
  data() {
    return {
      
    };
  },
};
</script>

<style scoped>
.banner {
  position: relative;
  overflow: hidden;
}
.text-center {
  text-align: center;
}
.text-md-end {
  text-align: right;
}
</style>
