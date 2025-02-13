import vuetify from './vuetify'
import router from '../router'
import VueApexCharts from 'vue3-apexcharts'
// Types
import type { App } from 'vue'


export function registerPlugins (app: App) {
  app
    .use(vuetify)
    .use(router)
    .use(VueApexCharts)
}
