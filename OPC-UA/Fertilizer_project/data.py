import asyncio
import websockets

async def receive_data():
    uri = "ws://localhost:8000"  # Replace with your WebSocket server URI
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                # Receive data from the WebSocket server
                data = await websocket.recv()
                print("Received:", data)
            except websockets.exceptions.ConnectionClosed:
                print("WebSocket connection closed.")
                break
            except Exception as e:
                print("Error:", e)

asyncio.run(receive_data())
