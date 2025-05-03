from typing import Dict
from fastapi import WebSocket
# Connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket
        print(f"{user_id} connected")

    def disconnect(self, user_id: str):
        self.active_connections.pop(user_id, None)
        print(f"{user_id} disconnected")

    async def send_personal_message(self, to_user_id: str, message: Dict):
        if to_user_id in self.active_connections:
            await self.active_connections[to_user_id].send_json(message)
        else:
            print(f"User {to_user_id} is not connected")
