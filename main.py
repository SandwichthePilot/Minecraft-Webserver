import asyncio
import os
import websockets
import json

async def handler(websocket):
    print("Minecraft connected!")
    try:
        while True:
            # Send a command to the game
            command = {
                "body": {
                    "commandLine": "weather rain",
                    "version": 1
                },
                "header": {
                    "requestId": "12345",
                    "messagePurpose": "commandRequest",
                    "version": 1
                }
            }
            await websocket.send(json.dumps(command))
            await asyncio.sleep(10) # Repeats every 10 seconds
    except websockets.exceptions.ConnectionClosed:
        print("Minecraft disconnected.")

async def main():
    # Render provides the PORT environment variable
    port = int(os.environ.get("PORT", 10000))
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
