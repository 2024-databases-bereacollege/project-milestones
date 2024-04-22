<template>
  <div>
    <h1>Volunteers</h1>
    <ul>
      <li v-for="volunteer in volunteers" :key="volunteer.VolunteerID">
        {{ volunteer.FirstName }} {{ volunteer.LastName }} - {{ volunteer.Email }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      volunteers: []
    };
  },
  mounted() {
    this.fetchVolunteers();
  },
  methods: {
    fetchVolunteers() {
      axios.get('http://127.0.0.1:5000/api/volunteers')
        .then(response => {
          this.volunteers = response.data;
        })
        .catch(error => {
          console.error('Error fetching volunteers:', error);
        });
    }
  }
}
</script>
