<template>
    <div class="app">
      <h1>Volunteer Information Form</h1>
      <form @submit.prevent="addRecord">
        <div class="input-group">
          <label>Volunteer that helped:</label>
          <input v-model="newRecord.volunteer" type="text" placeholder="Enter volunteer's name">
        </div>
        <div class="input-group">
          <label>Neighbor Name:</label>
          <input v-model="newRecord.neighborName" type="text" placeholder="Enter neighbor's name">
        </div>
        <div class="input-group">
          <label>Neighbor Last Name:</label>
          <input v-model="newRecord.neighborLastName" type="text" placeholder="Enter neighbor's last name">
        </div>
        <div class="input-group">
          <label>Services Provided:</label>
          <input v-model="newRecord.services" type="text" placeholder="Describe services provided">
        </div>
        <div class="input-group">
          <label>Changes in Inventory:</label>
          <input v-model="newRecord.inventoryChanges" type="text" placeholder="Detail inventory changes">
        </div>
        <button type="submit">Add Record</button>
      </form>
      <div class="records">
        <h2>Submitted Records</h2>
        <ul>
          <li v-for="record in records" :key="record.id">
            {{ record.volunteer }} - {{ record.neighborName }} {{ record.neighborLastName }} - {{ record.services }} - {{ record.inventoryChanges }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        records: [],
        newRecord: {
          volunteer: '',
          neighborName: '',
          neighborLastName: '',
          services: '',
          inventoryChanges: ''
        },
        nextId: 1
      };
    },
    methods: {
      addRecord() {
        const recordToAdd = {
          ...this.newRecord,
          id: this.nextId++
        };
        this.records.push(recordToAdd);
        this.newRecord = { volunteer: '', neighborName: '', neighborLastName: '', services: '', inventoryChanges: '' };
      }
    }
  }
  </script>
  
  <style>
  .app {
    max-width: 600px;
    margin: auto;
    padding: 20px;
  }
  
  .input-group {
    margin-bottom: 10px;
  }
  
  .input-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .input-group input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  button {
    padding: 10px 20px;
    cursor: pointer;
  }
  </style>
  