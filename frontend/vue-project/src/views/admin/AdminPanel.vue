<template>
  <v-container fluid>
    <v-row>
        <v-navigation-drawer permanent>
          <v-list>
            <v-list-item to="/admin/products" title="Zarządzanie produktami"></v-list-item>
          </v-list>
        </v-navigation-drawer>

      <v-col cols="12">
        <router-view></router-view>
      </v-col>
    </v-row>
  </v-container>
</template>