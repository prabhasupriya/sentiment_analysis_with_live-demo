from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from datetime import datetime
import asyncio

router = APIRouter()

@router.websocket("/ws/sentiment")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # 1️⃣ Send connection confirmation
    await websocket.send_json({
        "type": "connected",
        "message": "WebSocket connected",
        "timestamp": datetime.utcnow().isoformat()
    })

    try:
        # 2️⃣ Periodic metrics (every 30 seconds)
        while True:
            await asyncio.sleep(30)
            await websocket.send_json({
                "type": "metrics",
                "data": {
                    "total": 100,
                    "positive": 55,
                    "negative": 25,
                    "neutral": 20
                },
                "timestamp": datetime.utcnow().isoformat()
            })
    except WebSocketDisconnect:
        print("WebSocket disconnected")
