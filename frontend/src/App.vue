<template>
  <div> <!-- Single root element -->
    <div id="app">

      <Sidebar />


    </div>
    <router-view/>
  </div>
</template>

<script>
//import NavBar from './components/NavBar.vue';
import Sidebar from './components/Sidebar.vue';

export default {
  name: 'App',
  components: {
  //  NavBar,
    Sidebar
  }
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
.content {
  margin-left: 16rem; /* Push content to the right of the sidebar */
  padding: 1rem; /* Padding around content */
}
</style>
