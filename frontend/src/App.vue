<template>
  <div> <!-- Single root element -->
    <div id="app">
      <NavBar/>
      <router-link to="/">HomePage</router-link> |
      <router-link to="/test">Test</router-link>
      <router-link to="/loginPage">LoginPage</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>

<style>
#app {
  text-align: center;
  margin-top: 50px;
}
</style>
