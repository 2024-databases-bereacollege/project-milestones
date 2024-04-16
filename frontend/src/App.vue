<template>
  <div id="app">
    <CRUDTable />
  </div>
</template>

<script>
import CRUDTable from './components/CRUDTable.vue'; // Adjust the path as necessary

export default {
  name: 'App',
  components: {
    CRUDTable
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
