import asyncio
from dataloader import fetch_biker_traffic, get_client
from database import insert_data
from scripts.init_db import init_db


async def main():
    await init_db()

    async with get_client() as client:
        bike_traffic = await fetch_biker_traffic(client)
        await insert_data(bike_traffic)


if __name__ == "__main__":
    asyncio.run(main())
