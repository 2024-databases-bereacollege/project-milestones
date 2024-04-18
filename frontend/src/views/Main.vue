<template>
    <div class="Main">
      <div class="links">
        <router-link to="/Main">History</router-link> <!-- History is the default tab here -->
        <router-link to="/Main/contact">Contact</router-link>
        <router-link to ="Main/NeighborTable">NeighborTable</router-link>
      </div>
      <div class="content">
        <h1>DatabaseTables</h1>
        <router-view></router-view>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Main',
    props: {},
    data() {
      return {
      }
    }
  }
  </script>
  
  <style>
  .about {
    display: flex; /* Keep this to align items horizontally */
  }
  
  .links {
    display: flex;
    flex-direction: column; /* Stack links vertically */
    padding: 0; /* Adjust padding as needed */
    margin-right: 2rem; /* Space between links and content */
  }
  
  .links a {
    padding: 0.5rem; /* Adjust padding to your liking */
    text-decoration: none;
    background-color: #e7e7e7;
    color: #000000;
    margin-bottom: 1rem; /* Space between links */
  }
  
  .links .router-link-exact-active {
    background-color: #cc0000;
    color: #FFFFFF;
  }
  
  .content {
    flex-grow: 1; /* Allow the content area to fill the remaining space */
    background-color: #e7e7e7;
    padding: 1rem; /* Add padding around the content */
    height: auto; /* Adjust height as needed */
  }
  </style>
  