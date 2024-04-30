<template>
  <div class="neighbor-profile">
    <h2>{{ neighbor.FirstName }} {{ neighbor.LastName }}</h2>
    <table>
      <tr>
        <th><i class="fas fa-birthday-cake"></i> Date of Birth</th>
        <td>{{ neighbor.DateOfBirth }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-phone"></i> Phone</th>
        <td>{{ neighbor.Phone }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-map-marker-alt"></i> Location</th>
        <td>{{ neighbor.Location }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-envelope"></i> Email</th>
        <td>{{ neighbor.Email }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-calendar-plus"></i> Created Date</th>
        <td>{{ neighbor.Created_date }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-id-card"></i> Has State ID</th>
        <td>{{ neighbor.HasStateID ? 'Yes' : 'No' }}</td>
      </tr>
      <tr>
        <th><i class="fas fa-paw"></i> Has Pet</th>
        <td>{{ neighbor.HasPet ? 'Yes' : 'No' }}</td>
      </tr>
    </table>

    <h3>Visit Records</h3>
    <IndividualVisitLog :visits="visitRecords" />
  </div>
</template>

<script>
import IndividualVisitLog from './IndividualVisitLog.vue';

export default {
  components: {
    IndividualVisitLog,
  },
  data() {
    return {
      neighbor: {
        NeighborID: null,
        VolunteerID: null,
        OrganizationID: null,
        FirstName: '',
        LastName: '',
        DateOfBirth: null,
        Phone: '',
        Location: '',
        Email: '',
        Created_date: null,
        HasStateID: false,
        HasPet: false,
      },
      visitRecords: [],
    };
  },
  mounted() {
    const neighborID = this.$route.params.ID;
    
    axios.get(`http://127.0.0.1:5000/api/neighbors/${neighborID}`)
      .then(response => {
        this.neighbor = response.data;
      })
      .catch(error => {
        console.error(error);
      });

    // Fetch visit records from the API based on neighborID
    // Update the `visitRecords` data property with the fetched data
    // Example:
    // axios.get(`/api/neighbors/${neighborID}/visits`)
    //   .then(response => {
    //     this.visitRecords = response.data;
    //   })
    //   .catch(error => {
    //     console.error(error);
    //   });
  },
};
</script>

<style scoped>
.neighbor-profile {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

th,
td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  font-weight: bold;
}

i {
  margin-right: 5px;
}
</style>




<!-- <template>
    <div class="neighbor-profile">
      <h2>{{ Neighbor.FirstName }} {{ Neighbor.NastName }}</h2>
      <table>
        -- Display neighbor information in a table --
        <tr>
          <th>Date of Birth</th>
          <td>{{ Neighbor.DateOfBirth }}</td>
        </tr>
        <-- Add more rows for other neighbor information --
      </table>
  
      <h3>Visit Records</h3>
      <VisitRecords :visits="visitRecords" />
    </div>
  </template>
  
  <script>
  import IndividualVisitLog from './IndividualVisitLog.vue';
  
  export default {
    components: {
      IndividualVisitLog,
    },
    data() {
      return {
        Neighbor: {},
        visitRecords: [],
      };
    },
    mounted() {
      const NeighborID = this.$route.params.ID;
      // Fetch neighbor information and visit records from the API
      // Update the `neighbor` and `visitRecords` data properties
    },
  };
  </script> -->
