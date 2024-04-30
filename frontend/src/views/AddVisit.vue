<template>
  <div>
    <h2>Add visit information</h2>
    <ComboboxSelect
      v-for="(items, index) in apiData"
      :key="index"
      :items="items"
      :label="`Select ${index + 1}`"
      @update:model-value="selectedValues[index] = $event"
    />
    <button @click="submitData">Submit</button>
  </div>
</template>

<script>
import ComboboxSelect from '@/components/ComboboxSelect.vue';
import axios from 'axios';

export default {
  components: {
    ComboboxSelect,
  },
  data() {
    return {
      apiData: [],
      selectedValues: [],
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/Add_Visit');
        this.apiData = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async submitData() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/api/update_database', {
          selectedValues: this.selectedValues,
        });
        console.log('Data submitted successfully:', response.data);
        // Handle success response
      } catch (error) {
        console.error('Error submitting data:', error);
        // Handle error
        }
      },
  },
};
</script>
