<template>
    <div class="sidebar">
      <!-- router -->
      <router-link to="/">HomePage</router-link> 
      <router-link to="/Add_Visit">Add Visit</router-link>  
      <router-link to="/login_page">Login Page</router-link>
      <router-link to="/Volunteers">Volunteers</router-link>
      <router-link to="/Neighbors">Neighbors</router-link>
      <router-link to="/Visit_Records">Visit Record</router-link>
      <router-link to="/Services">Services</router-link>
      <router-link to="/Service_Providers">Service Providers</router-link>
      <router-link to="/Inventory">Inventory</router-link>
    <!--   <router-link to="/test">Test</router-link> -->
    <!--   <router-link to="/TestCRUD"> TestCRUD</router-link> -->

      </div>
    </template>
    
    <style>
    .sidebar {
      width: 16rem; /* Set the width of the sidebar */
      background-color: rgb(122, 211, 255); /* Shaded background */
      height: 100vh; /* Full viewport height */
      position: fixed; /* Fix position to the left */
      left: 0;
      top: 0;
      display: flex;
      flex-direction: column; /* Stack links vertically */
      padding: 1rem; /* Adjust padding as needed */
    }
    .sidebar a {
      margin-bottom: 1rem; /* Space between links */
      text-decoration: none;
      color: rgb(0, 0, 0);
    }
    </style>
  