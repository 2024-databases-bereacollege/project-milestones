<template>
  <div id="app">
    <header>
      <NavBar />
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
