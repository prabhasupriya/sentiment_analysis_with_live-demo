from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import asyncio

app = FastAPI()

# CORS for React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.websocket("/ws/sentiment")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("✅ WebSocket client connected")

    try:
        while True:
            await asyncio.sleep(2)
            await websocket.send_json({
                "type": "sentiment",
                "positive": 5,
                "negative": 2,
                "neutral": 3,
                "timestamp": datetime.utcnow().isoformat()
            })
    except WebSocketDisconnect:
        print("❌ WebSocket client disconnected")
