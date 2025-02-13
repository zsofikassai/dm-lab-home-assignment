import logging
from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
import httpx

app = FastAPI()

BASE_URL = "https://www.eco-visio.net/api/aladdin/1.0.0/pbl/publicwebpageplus/data"

LOCATION_PARAMS = {
    "Bem": {"idPdc": "100042789", "flowIds": "101042789;102042789"},
    "Árpád": {
        "idPdc": "100033984",
        "flowIds": "101033984;102033984;103033984;104033984",
    },
    "Hungária": {
        "idPdc": "100033987",
        "flowIds": "101033987;102033987;103033987;104033987",
    },
}

QUERY_PARAMS = {
    "idOrganisme": "809",
    "fin": "31/12/2024",
    "debut": "01/01/2020",
    "interval": "4",
}


@asynccontextmanager
async def get_client():
    async with httpx.AsyncClient() as client:
        yield client


@app.get("/fetch-biker-traffic")
async def fetch_biker_traffic(client: httpx.AsyncClient = Depends(get_client)):
    biker_traffic = []

    for location, params in LOCATION_PARAMS.items():
        api_url = f"{BASE_URL}/{params['idPdc']}"

        try:
            response = await client.get(api_url, params={**QUERY_PARAMS, **params})
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logging.error(f"HTTP error {e.response.status_code} for {location}: {e}")
            raise HTTPException(status_code=e.response.status_code, detail=f"Failed to fetch traffic data for {location}")

        biker_traffic.append({"location": location, "data": response.json()})
    return biker_traffic
