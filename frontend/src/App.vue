<template>
  <div id="app">
    <TestComponent />
  </div>
</template>

<script>
import TestComponent from './components/TestComponent.vue'; 

export default {
  name: 'App',
  components: {
    TestComponent
  }
}
</script>

<style>
/* Your styles here */
#app {
  text-align: center;
  margin-top: 50px;
}
</style>
