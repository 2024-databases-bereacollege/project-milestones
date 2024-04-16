<template>
  <div id="app">
    <TestComponent />
    <CRUDTable />
  </div>
</template>

<script>
import TestComponent from './components/TestComponent.vue';

export default {
  name: 'App',
  components: {
    TestComponent,
    
  }
}
</script>

<style>

#app {
  text-align: center;
  margin-top: 50px;
}
</style>
