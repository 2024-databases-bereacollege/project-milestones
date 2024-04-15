// router/index.js
import Vue from "vue";
import VueRouter from "vue-router";
import { createRouter, createWebHistory } from 'vue-router' //TODO not sure if needed
import CRUDTABLE from "@/components/CRUDTABLE.vue";

// Import components
import HomePage from '@/components/HomePage.vue'
import LoginPage from '@/components/LoginPage.vue'
// Import other components for routes

const routes = [
  { path: '/', component: HomePage },
  { path: '/login', component: LoginPage },
    { path: '/crudtable', name : 'crudtable', component: CRUDTABLE },

  // Define other routes here
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
