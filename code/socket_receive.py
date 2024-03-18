import asyncio
import websockets
import socket_demo as sd
import threading


async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message from client: {message}")
        if message == 'start':
            sd.flag = 1
        elif message == 'stop':
            sd.flag = 0


def main():
    start_server = websockets.serve(handle_client, "localhost", 12345)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == "__main__":
    thread = threading.Thread(target=main, args=())
    thread.start()
    while True:
        print(sd.flag)
