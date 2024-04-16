// router/index.js

import { createRouter, createWebHistory } from 'vue-router' 

// Import components
import CRUDTable from "@/components/CRUDTable.vue";
//import HomePage from '@/components/HomePage.vue'
//import LoginPage from '@/components/LoginPage.vue'
// Import other components for routes

const routes = [
    { path: '/', name : 'home', component: CRUDTable },
 // { path: '/', component: HomePage },
//  { path: '/login', component: LoginPage },
  //  { path: '/crudtable', name : 'crudtable', component: CRUDTable },

  // Define other routes here
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router;
