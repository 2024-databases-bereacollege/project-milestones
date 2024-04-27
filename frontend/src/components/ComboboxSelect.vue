<template>
  <v-combobox
    chips
    multiple
    label="Select"
    :items="items"
    variant="outlined"
  ></v-combobox>
</template>

<script>
export default {
  name: 'ComboboxSelect',
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
};
</script>
