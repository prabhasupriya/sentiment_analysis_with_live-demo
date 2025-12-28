from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio
from datetime import datetime, timezone
import random

router = APIRouter()

@router.websocket("/ws/sentiment")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket client connected")

    try:
        while True:
            positive = random.randint(10, 60)
            negative = random.randint(5, 30)
            neutral = random.randint(5, 40)

            total = positive + negative + neutral

            message = {
                "type": "sentiment_update",
                "distribution": {
                    "positive": positive,
                    "negative": negative,
                    "neutral": neutral
                },
                "metrics": {
                    "total": total,
                    "positive": positive,
                    "negative": negative,
                    "neutral": neutral
                },
                "trend": {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "positive": positive,
                    "negative": negative,
                    "neutral": neutral
                },
                "post": {
                    "id": random.randint(1, 10000),
                    "content": "Live sentiment message",
                    "sentiment": random.choice(["positive", "negative", "neutral"]),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
            }

            await websocket.send_json(message)
            await asyncio.sleep(2)

    except WebSocketDisconnect:
        print("❌ WebSocket client disconnected")
