from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncpg
from database import get_db
from calculations import calculate_traffic_stats, calculate_yearly_sums


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/get-stats-by-location")
async def get_stats_by_location(db: asyncpg.Connection = Depends(get_db)):
    try:
        data = await calculate_traffic_stats(db)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't load stats"
            )
        return {"status": status.HTTP_200_OK, "data": data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}",
        )


@app.get("/api/get-yearly-traffic")
async def get_yearly_traffic(db: asyncpg.Connection = Depends(get_db)):
    try:
        data = await calculate_yearly_sums(db)
        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Couldn't load yearly traffic data",
            )
        return {"status": status.HTTP_200_OK, "data": data}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal Server Error: {str(e)}",
        )
