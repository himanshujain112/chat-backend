import asyncio
import websockets
import json

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoidXNlcl8xIn0._15323syXKAPRqXvP2J-BwjNmKI0tlC043y5biqP1-Y"

async def test_chat():
    uri = f"ws://127.0.0.1:3000/ws/chat?token={TOKEN}"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            "to": "user_2",
            "message": "Hello from user_1!"
        }))
        response = await websocket.recv()
        print("Received:", response)

asyncio.run(test_chat())
