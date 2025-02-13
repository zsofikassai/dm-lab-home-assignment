import asyncpg
import os
import logging

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/db")


async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)


async def init_db():
    conn = await get_db_connection()
    try:
            await conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS bike_traffic (
                        id SERIAL PRIMARY KEY,
                        location VARCHAR(50) NOT NULL,
                        date DATE NOT NULL,
                        count INT NOT NULL,
                        created_at TIMESTAMP DEFAULT NOW(),
                        UNIQUE (location, date)
                    );
                    """
            )
    except asyncpg.PostgresError as e:
        logging.error(f"Database error: {e}")
    finally:
        await conn.close()

