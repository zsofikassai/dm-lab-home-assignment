<script setup>
const props = defineProps({
  title: String,
  value: [String, Number],
});
</script>

<template>
  <VCard class="p-4" rounded="lg" variant="outlined">
    <template #title>
      <h2 class="text-h5 font-weight-bold">{{ props.value }}</h2>
    </template>

    <template #subtitle>
      <div>{{ props.title }}</div>
    </template>
  </VCard>
</template>
