<template>
  <div id="app">
    <header>
      <NavBar />

      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
        <router-link to="/crudtable">CRUD Table</router-link>
      </nav>
    </header>
    <main>
      <router-view></router-view>
      <HelloWorld/>
    </main>
  </div>
</template>



<script>
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
export default {
  name: 'App',

  components: {
    HelloWorld,
    NavBar,
  },

  data: () => ({
    //
  }),
}
</script>

<style>
/* Your CSS here */
</style>
