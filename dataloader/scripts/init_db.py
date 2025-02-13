import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/db")

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    cur.execute(
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

    conn.commit()
    cur.close()
    conn.close()

