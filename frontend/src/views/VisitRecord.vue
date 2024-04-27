<template>
  <div>
    <data-table
      :edited-item="editedItem"
      @update:edited-item="updateEditedItem"
      @save="saveItem"
      :headers="tableHeaders"
      :items="tableItems"
      :default-item="defaultItem"
      @edit-item="editItem"
      @delete-item="deleteItem"
      @delete-item-confirm="deleteItemConfirm"
      @close="close"
      @close-delete="closeDelete"
      sort-by="calories"
      sort-order="asc"
    ></data-table>
  </div>
</template>

<script>
import DataTable from '@/components/DataTable.vue';

export default {
  components: {
    DataTable,
  },
  data() {
    return {
      tableHeaders: [
        { title: 'Dessert (100g serving)', key: 'name' },
        { title: 'Calories', key: 'calories' },
        { title: 'Fat (g)', key: 'fat' },
        { title: 'Carbs (g)', key: 'carbs' },
        { title: 'Protein (g)', key: 'protein' },
        { title: 'Actions', key: 'actions', sortable: false },
      ],
      tableItems: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
        },
        // Add more items as needed
      ],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
    };
  },
  methods: {
    editItem(item) {
      this.editedIndex = this.tableItems.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },
    deleteItem(item) {
      this.editedIndex = this.tableItems.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },
    deleteItemConfirm() {
      // Perform the delete operation in the database
      // Remove the item from the tableItems array
      this.tableItems.splice(this.editedIndex, 1);
      this.closeDelete();
    },
    close() {
      this.editedIndex = -1;
      this.editedItem = Object.assign({}, this.defaultItem);
    },
    closeDelete() {
      this.editedIndex = -1;
      this.editedItem = Object.assign({}, this.defaultItem);
    },
    updateEditedItem(item) {
      this.editedItem = item;
    },
    saveItem(item) {
      if (this.editedIndex > -1) {
        // Perform the update operation in the database
        Object.assign(this.tableItems[this.editedIndex], item);
      } else {
        // Perform the create operation in the database
        this.tableItems.push(item);
      }
      this.close();
    },
  },
};
</script>
