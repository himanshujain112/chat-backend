from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from auth import get_current_user
from connection_manager import ConnectionManager
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


conn_manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    print(token)
    if not token:
        await websocket.close(code=1008)
        print("Connection closed due to missing token.")
        return

    user_id = get_current_user(token)
    if not user_id:
        await websocket.close(code=1008)
        print("Invalid token. Connection closed.")
        return

    await conn_manager.connect(user_id, websocket)
    print(f"User {user_id} connected successfully.")

    try:
        while True:
            data = await websocket.receive_json()
            to_user = data.get("to")
            message = data.get("message")

            if to_user and message:
                await conn_manager.send_personal_message(to_user, {
                    "from": user_id,
                    "message": message
                })
    except WebSocketDisconnect:
        conn_manager.disconnect(user_id)
        print(f"User {user_id} disconnected.")
