<template>
  <div>
    <h1>Message from Backend:</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TestComponent',
  data() {
    return {
      message: '',
    };
  },
  methods: {
    fetchMessage() {
      axios.get('http://localhost:5000/test')
        .then(response => {
          this.message = response.data.message;
        })
        .catch(error => {
          console.error('There was an error fetching the message:', error);
        });
    },
  },
  mounted() {
    this.fetchMessage();
  },
};
</script>
