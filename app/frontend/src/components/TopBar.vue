<!-- TopBar.vue -->
<template>
    <div class="top-bar">
      <!--<div class="logo">
        <img :src="logo" alt="UP Initiative Logo" />
      </div> -->
      <h1 class="organization-name">UP Initiative</h1>
    </div>
  </template>
  
  <script>
  //import logo from '../assets/UPLOGO.PNG';
  
  export default {
    name: 'TopBar',
    data() {
      return {
       // logo,
      };
    },
  };
  </script>
  
  <style scoped>
  
  .top-bar {
    margin-left: 16rem; /* Push content to the right of the sidebar */
    display: flex;
    align-items: center;
  background-color: #9c97ff;
  padding: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 0;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999;
  }
  
  .logo {
  margin-right: 1rem;
  position: relative;
  z-index: 1000;
}
  
  .logo img {
    height: 40px;
  }
  
  .organization-name {
  margin-left: 16rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: #333;
  margin: 0;
}
  </style>
