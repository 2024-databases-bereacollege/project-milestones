// router/index.js

import { createRouter, createWebHistory } from 'vue-router' 

// Import components
import TestComponent from '@/components/TestComponent.vue';
import CRUDTable from "@/components/CRUDTable.vue";
import HomeView from "@/components/HomeView.vue";
import LoginPage from "@/components/LoginPage.vue";
// Import other components for routes

const routes = [
    //{ path: '/', name : 'home', component: CRUDTable },
    { path: '/test', name : 'test', component: TestComponent},
    { path: '/', component: HomeView },
    { path: '/login', component: LoginPage },
    { path: '/crudtable', name : 'crudtable', component: CRUDTable },

  // Define other routes here
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes // maybe , is needed here?
})

export default router // maybe ; is needed here?
