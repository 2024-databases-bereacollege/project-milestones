import { createRouter, createWebHistory } from 'vue-router';

// Import Views Components
import HomeView from "@/views/HomeView.vue";
import LoginPage from "@/views/LoginPage.vue";
import ServiceProviders from '@/views/ServiceProviders.vue';
import Services from '@/views/Services.vue';
import VolunteerTable from '@/views/VolunteerTable.vue';
import NeighborTable from '@/views/NeighborTable.vue';
import VisitRecord from '@/views/VisitRecord.vue';
import Inventory from '@/views/Inventory.vue';
import TestComponent from '@/components/TestComponent.vue';
import TestCRUD from '@/views/TestCRUD.vue';
import AddVisit from '@/views/AddVisit.vue';


const routes = [
    { 
        path: '/', 
        redirect: '/home', // Redirect root to home as a default route
    },
    { 
        path: '/home', 
        component: HomeView,
    },
    { 
        path: '/login_page', 
        component: LoginPage,
    },
    { path: '/Service_Providers', component: ServiceProviders },
    { path: '/Services', component: Services },
    { path: '/Volunteers', component: VolunteerTable },
    { path: '/Neighbors', component: NeighborTable },
    { path: '/Visit_Records', component: VisitRecord },
    { path: '/Inventory', component: Inventory },
    { path: '/test', component: TestComponent},
    { path: '/testcrud', component: TestCRUD},
    { path: '/Add_Visit', component: AddVisit},
    { path: '/:pathMatch(.*)*', redirect: '/home' } // Redirect all other paths to home
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes 
});

export default router;







// // router/index.js

// import { createRouter, createWebHistory } from 'vue-router' 

// // Import components
// import TestComponent from '@/components/TestComponent.vue';


// // Import Views Components
// import App from "@/App.vue";
// import HomeView from "@/views/HomeView.vue";
// import LoginPage from "@/views/LoginPage.vue";
// import ServiceProviders from '@/views/ServiceProviders.vue';
// import Services from '@/views/Services.vue';
// import VolunteerTable from '@/views/VolunteerTable.vue';
// import NeighborTable from '@/views/NeighborTable.vue';
// import VisitRecord from '@/views/VisitRecord.vue';
// import Inventory from '@/views/Inventory.vue';

// // Import other components for routes

// const routes = [
//     //{ path: '/', name : 'home', component: CRUDTable },

//     { path: '/App', name: 'App',
//       // route level code-splitting
//       // this generates a separate chunk (Main.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import(/* webpackChunkName: "Main" */ '../App.vue'),
//       children: [
//         { path: '', component: App }, // default tab that shows on /Main route
//         { path: '/ServiceProviders', name : 'ServiceProviders', component: ServiceProviders },
//         { path: '/test', name : 'test', component: TestComponent},
//         { path: '/', component: HomeView },
//         { path: '/login', component: LoginPage },
//         { path: '/Services', name : 'Services', component: Services },
//         { path: '/VolunteerTable', name : 'VolunteerTable', component: VolunteerTable },
//         { path: '/NeighborTable', name : 'NeighborTable', component: NeighborTable },
//         { path: '/VisitRecord', name : 'VisitRecord', component: VisitRecord },
//         { path: '/inventory', name : 'inventory', component: Inventory}

//       ]
//     }
// ]

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes 
// })

// export default router 
