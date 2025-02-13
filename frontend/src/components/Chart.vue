<script setup lang="ts">
import { defineProps, computed } from "vue";
import type { YearlyTrafficItem } from "@/types";

const props = defineProps<{
  location: string;
  data: YearlyTrafficItem[];
}>();

const chartSeries = computed(() => [
  {
    name: "Bike Traffic",
    data: props.data.map((item) => item.count),
  },
]);

const chartOptions = computed(() => ({
  chart: {
    type: "line",
    toolbar: {
      show: false,
    },
  },
  stroke: {
    curve: "smooth",
  },
  xaxis: {
    categories: props.data.map((item) => item.year),
    title: {
      text: "Year",
    },
  },
  yaxis: {
    title: {
      text: "Bike Count",
    },
  },
  tooltip: {
    enabled: true,
  },
  markers: {
    size: 4,
  },
}));
</script>

<template>
  <VCard class="p-4 mb-4 mx-auto" min-width="600">
    <template #title>
      {{ location }}
    </template>
    <template #text>
      <apexchart
        width="100%"
        height="300"
        type="line"
        :options="chartOptions"
        :series="chartSeries"
      />
    </template>
  </VCard>
</template>
