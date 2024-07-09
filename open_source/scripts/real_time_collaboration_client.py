python
import asyncio
import websockets

# WebSocket client
async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("Enter a message to send: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received response: {response}")

if __name__ == "__main__":
    asyncio.run(main())
