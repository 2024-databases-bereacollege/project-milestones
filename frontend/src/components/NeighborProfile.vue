<template>
    <div class="neighbor-profile">
      <h2>{{ Neighbor.FirstName }} {{ Neighbor.NastName }}</h2>
      <table>
        <!-- Display neighbor information in a table -->
        <tr>
          <th>Date of Birth</th>
          <td>{{ Neighbor.DateOfBirth }}</td>
        </tr>
        <!-- Add more rows for other neighbor information -->
      </table>
  
      <h3>Visit Records</h3>
      <VisitRecords :visits="visitRecords" />
    </div>
  </template>
  
  <script>
  import VisitRecords from './VisitRecords.vue';
  
  export default {
    components: {
      VisitRecords,
    },
    data() {
      return {
        Neighbor: {},
        visitRecords: [],
      };
    },
    mounted() {
      const NeighborID = this.$route.params.id;
      // Fetch neighbor information and visit records from the API
      // Update the `neighbor` and `visitRecords` data properties
    },
  };
  </script>
