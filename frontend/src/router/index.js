// router/index.js

import { createRouter, createWebHistory } from 'vue-router' 

// Import components
import TestComponent from '@/components/TestComponent.vue';
import CRUDTable from "@/components/CRUDTable.vue";
import HomeView from "@/components/HomeView.vue";
import LoginPage from "@/components/LoginPage.vue";

// Import Views Components
import Contact from '@/views/Contact.vue';
import History from '@/views/History.vue';
// Import other components for routes

const routes = [
    //{ path: '/', name : 'home', component: CRUDTable },
    { path: '/test', name : 'test', component: TestComponent},
    { path: '/', component: HomeView },
    { path: '/login', component: LoginPage },
    { path: '/crudtable', name : 'crudtable', component: CRUDTable },

    { path: '/contact', name : 'contact', component: Contact },
    { path: '/history', name : 'history', component: History },
    {
      path: '/Main',
      name: 'Main',
      // route level code-splitting
      // this generates a separate chunk (Main.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Main" */ '../views/Main.vue'),
      children: [
        { path: '', component: History }, // default tab that shows on /Main route
        { path: 'contact', component: Contact }
      ]
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes 
})

export default router 
