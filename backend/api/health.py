from fastapi import APIRouter
from sqlalchemy import text
from datetime import datetime, timezone

from backend.models.database import async_session
from backend.redis_client import redis_client

router = APIRouter()

@router.get("/api/health")
async def health_check():
    db_status = "unknown"
    redis_status = "unknown"

    # DB check
    try:
        async with async_session() as session:
            await session.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"

    # Redis check
    try:
        await redis_client.ping()
        redis_status = "connected"
    except Exception:
        redis_status = "disconnected"

    return {
        "status": "healthy" if db_status == "connected" else "degraded",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {
            "database": db_status,
            "redis": redis_status
        }
    }
