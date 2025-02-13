export interface TrafficData {
  location: string;
  min_traffic_day: string;
  max_traffic_day: string;
  total_traffic: number;
}

export interface YearlyTrafficEntry {
  year: number;
  count: number;
}

export type YearlyTrafficData = Record<string, YearlyTrafficEntry[]>;
