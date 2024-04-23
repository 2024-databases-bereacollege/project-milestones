<template>
    <div class="sidebar">
      <router-link to="/">HomePage</router-link> 
      <router-link to="/login">LoginPage</router-link>
      <router-link to="/VolunteerTable">VolunteerTable</router-link>
      <router-link to="/NeighborTable">NeighborTable</router-link>
      <router-link to="/VisitRecord">VisitRecord</router-link>
      <router-link to="/Services">Services</router-link>
      <router-link to="/ServiceProviders">ServiceProviders</router-link>
      <router-link to="/Inventory">Inventory</router-link>
      <router-link to="/test">Test</router-link>

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
  