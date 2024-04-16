<template>
    <v-navigation-drawer app :width="199">
      <v-list-item title="UP Initiative" subtitle="Navigation Bar"></v-list-item>
      <v-divider></v-divider>
      <!-- Update list items to use router-link -->
      <v-list-item link>
        <router-link to="/">Home</router-link>
      </v-list-item>
      <v-list-item link>
        <router-link to="/crudtable">CRUD Table</router-link>
      </v-list-item>
      <v-list-item link>
        <router-link to="/neighbor">Neighbors</router-link>
      </v-list-item>
      <!-- Add more list items as needed -->
    </v-navigation-drawer>
  </template>
  
  <script>
  export default {
    name: 'NavigationDrawer',
  };
  </script>
  