// router/index.js

import { createRouter, createWebHistory } from 'vue-router' 

// Import components
import TestComponent from '@/components/TestComponent.vue';


// Import Views Components
import Main from "@/views/Main.vue";
import HomeView from "@/views/HomeView.vue";
import LoginPage from "@/views/LoginPage.vue";
import ServiceProviders from '@/views/ServiceProviders.vue';
import Services from '@/views/Services.vue';
import VolunteerTable from '@/views/VolunteerTable.vue';
import NeighborTable from '@/views/NeighborTable.vue';
import VisitRecord from '@/views/VisitRecord.vue';

// Import other components for routes

const routes = [
    //{ path: '/', name : 'home', component: CRUDTable },

    { path: '/Main', name: 'Main',
      // route level code-splitting
      // this generates a separate chunk (Main.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "Main" */ '../views/Main.vue'),
      children: [
        { path: '', component: Main }, // default tab that shows on /Main route
        { path: '/ServiceProviders', name : 'ServiceProviders', component: ServiceProviders },
        { path: '/test', name : 'test', component: TestComponent},
        { path: '/', component: HomeView },
        { path: '/login', component: LoginPage },
        { path: '/Services', name : 'Services', component: Services },
        { path: '/VolunteerTable', name : 'VolunteerTable', component: VolunteerTable },
        { path: '/NeighborTable', name : 'NeighborTable', component: NeighborTable },
        { path: '/VisitRecord', name : 'VisitRecord', component: VisitRecord }

      ]
    }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes 
})

export default router 
