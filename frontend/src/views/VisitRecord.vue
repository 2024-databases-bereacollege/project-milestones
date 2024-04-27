<template>
  <div>
    <data-table
      :headers="tableHeaders"
      :items="tableItems"
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
    };
  },
};
</script>
