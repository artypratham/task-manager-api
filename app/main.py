from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.dependencies import get_db

app = FastAPI(title ="Task Manager API", version="0.1.0")

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"status" : "ok", "db" : result.scalar()}