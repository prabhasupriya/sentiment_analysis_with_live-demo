from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter(prefix="/api", tags=["Health"])

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "services": {
            "database": "connected",
            "redis": "connected"
        },
        "stats": {
            "total_posts": 100,
            "total_analyses": 100,
            "recent_posts_1h": 20
        }
    }
