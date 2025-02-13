import asyncpg
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/db")


async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
