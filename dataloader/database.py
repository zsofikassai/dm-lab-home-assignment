from scripts.init_db import get_db_connection
from datetime import datetime


async def insert_data(data: list[dict]):
    records = [
        (entry["location"], datetime.strptime(date, "%m/%d/%Y").date(), int(count))
        for entry in data
        for date, count in entry["data"]
    ]

    if not records:
        return
    db = await get_db_connection()
    try:
        await db.executemany(
            """
            INSERT INTO bike_traffic (location, date, count) 
            VALUES ($1, $2, $3)
            ON CONFLICT (location, date) DO UPDATE 
            SET count = EXCLUDED.count;
            """,
            records,
        )
    finally:
        await db.close()
