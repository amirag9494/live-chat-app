from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, FileResponse
from typing import List
import json

app = FastAPI()

# Connection Manager to keep track of active connections and broadcast messages
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        # Send the message to all connected clients
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

# Serve index.html directly from the root directory
@app.get("/", response_class=HTMLResponse)
async def get():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

# Serve CSS file directly from the root directory
@app.get("/style.css")
async def get_css():
    return FileResponse("style.css", media_type="text/css")

# Serve JavaScript file directly from the root directory
@app.get("/script.js")
async def get_js():
    return FileResponse("script.js", media_type="application/javascript")

# WebSocket endpoint for real-time chat communication
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Receive incoming JSON text data from the client
            data = await websocket.receive_text()
            packet = json.loads(data)
            sender = packet.get("sender")
            message = packet.get("message")
            
            # Broadcast the message including the sender's username to everyone
            await manager.broadcast(f"{sender}: {message}")
    except WebSocketDisconnect:
        # Handle client disconnection and notify other users
        manager.disconnect(websocket)
        await manager.broadcast("System: A user left the chat.")