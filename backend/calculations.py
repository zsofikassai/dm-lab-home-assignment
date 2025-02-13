from database import get_db
import pandas as pd
import asyncpg
from fastapi import Depends


async def calculate_traffic_stats(db: asyncpg.Connection = Depends(get_db)):
    query = "SELECT location, date, count FROM bike_traffic;"
    results = await db.fetch(query)

    df = pd.DataFrame(results, columns=["location", "date", "count"])

    if df.empty:
        return []

    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna(subset=["date"])

    df["weekday"] = df["date"].dt.day_name()

    weekday_avg = df.groupby(["location", "weekday"], as_index=False)["count"].mean()

    max_traffic_days = weekday_avg.loc[
        weekday_avg.groupby("location")["count"].idxmax()
    ]
    min_traffic_days = weekday_avg.loc[
        weekday_avg.groupby("location")["count"].idxmin()
    ]

    total_traffic_by_location = df.groupby("location", as_index=False)["count"].sum()

    result = {
        location: {
            "min_traffic_day": min_traffic_days[min_traffic_days["location"] == location]["weekday"].values[0],
            "max_traffic_day": max_traffic_days[max_traffic_days["location"] == location]["weekday"].values[0],
            "total_traffic": int(total_traffic_by_location[total_traffic_by_location["location"] == location]["count"].values[0]),
        }
        for location in df["location"]
    }

    return result


async def calculate_yearly_sums(db: asyncpg.Connection = Depends(get_db)):
    query = "SELECT location, date, count FROM bike_traffic;"
    results = await db.fetch(query)

    df = pd.DataFrame(results, columns=["location", "date", "count"])

    if df.empty:
        return {}

    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year

    yearly_sums = df.groupby(["location", "year"])["count"].sum().reset_index()

    yearly_data = {
        location: group[["year", "count"]].to_dict(orient="records")
        for location, group in yearly_sums.groupby("location")
    }

    return yearly_data


