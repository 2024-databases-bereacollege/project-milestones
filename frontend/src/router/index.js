// router/index.js
//import Vue from "vue"; seems to be for vue2
//import VueRouter from "vue-router"; seems to be for vue2
import { createRouter, createWebHistory } from 'vue-router' //TODO not sure if needed
import CRUDTable from "@/components/CRUDTable.vue";

// Import components
//import HomePage from '@/components/HomePage.vue'
//import LoginPage from '@/components/LoginPage.vue'
// Import other components for routes

const routes = [
 // { path: '/', component: HomePage },
//  { path: '/login', component: LoginPage },
    { path: '/CRUDTable', name : 'crudtable', component: CRUDTable },

  // Define other routes here
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router;
