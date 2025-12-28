# main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from datetime import datetime

app = FastAPI()

clients = set()

@app.websocket("/ws/sentiment")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.add(websocket)
    
    # Send a connection confirmation
    await websocket.send_json({
        "type": "connected",
        "message": "WebSocket connected",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })
    
    try:
        while True:
            data = await websocket.receive_text()  # you can receive data if needed
            # For demo, just echo back
            await websocket.send_json({
                "type": "message",
                "message": data,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            })
    except WebSocketDisconnect:
        clients.remove(websocket)
        print("Client disconnected")
