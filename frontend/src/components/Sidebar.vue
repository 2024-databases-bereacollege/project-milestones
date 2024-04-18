<template>
    <div class="sidebar">
      <router-link to="/loginPage">LoginPage</router-link>
      <router-link to="/">HomePage</router-link> |
      <router-link to="/about">History</router-link>
      <router-link to="/about/contact">Contact</router-link>
      <router-link to="/about/NeighborTable">NeighborTable</router-link>
      <router-link to="/test">Test</router-link>
    </div>
  </template>
  
  <style>
  .sidebar {
    width: 16rem; /* Set the width of the sidebar */
    background-color: #e7e7e7; /* Shaded background */
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
    color: #000000;
  }
  </style>
  