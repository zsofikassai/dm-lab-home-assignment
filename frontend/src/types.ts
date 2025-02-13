export interface TrafficStatsItem {
  min_traffic_day: string;
  max_traffic_day: string;
  total_traffic: number;
}

export type TrafficStats = Record<string, TrafficStatsItem>;

export interface YearlyTrafficItem {
  year: number;
  count: number;
}

export type YearlyTrafficData = Record<string, YearlyTrafficItem[]>;
