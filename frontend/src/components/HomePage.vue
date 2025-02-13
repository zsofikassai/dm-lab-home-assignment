<template>
  <VResponsive class="align-center fill-height">
    <VContainer
      v-if="Object.keys(trafficData).length && Object.keys(yearlyData).length"
      class="d-flex justify-center"
    >
      <VCard class="pa-4">
        <template #title>
          <div>Traffic Statistics</div>
        </template>
        <template #subtitle>
          <div>2020/01/01 - 2024/12/31</div>
        </template>

        <VTabs v-model="activeTab" grow class="mb-4">
          <VTab v-for="(location, index) in locations" :key="index">
            {{ location }}
          </VTab>
        </VTabs>

        <VWindow v-model="activeTab">
          <VWindowItem v-for="(location, index) in locations" :key="index">
            <VContainer class="py-4">
              <VRow class="gap-y-4" align="start">
                <VCol cols="3">
                  <StatCard
                    title="Total traffic"
                    :value="trafficData[location].total_traffic"
                  />
                  <StatCard
                    title="Busiest Day"
                    :value="trafficData[location].max_traffic_day"
                    class="mt-4"
                  />
                  <StatCard
                    title="Least Busy Day"
                    :value="trafficData[location].min_traffic_day"
                    class="mt-4"
                  />
                </VCol>
                <VCol cols="6">
                  <Chart
                    :key="location"
                    :location="location"
                    :data="yearlyData[location]"
                  />
                </VCol>
              </VRow>
            </VContainer>
          </VWindowItem>
        </VWindow>
      </VCard>
    </VContainer>
  </VResponsive>
</template>

<script setup lang="ts">
import api from "@/api";
import type { TrafficStats, YearlyTrafficData } from "@/types";
import Chart from "@/components/Chart.vue";

const yearlyData = ref<YearlyTrafficData>({});

const trafficData = ref<TrafficStats[]>([]);
const activeTab = ref(0);
const locations = computed(() => Object.keys(trafficData.value));

const fetchYearlyTrafficData = async () => {
  try {
    const response = await api.get("get-yearly-traffic");
    return response.data.data;
  } catch (err) {
    console.error("Error fetching data:", err);
  }
};

const fetchTrafficStats = async () => {
  try {
    const response = await api.get("/get-stats-by-location");
    return response.data.data;
  } catch (err) {
    console.error("Error fetching data:", err);
  }
};

onMounted(async () => {
  trafficData.value = await fetchTrafficStats();
  yearlyData.value = await fetchYearlyTrafficData();
});
</script>
