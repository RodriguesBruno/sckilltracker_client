import json
import logging

from fastapi import WebSocket
from starlette.websockets import WebSocketState


class ConnectionManager:
    def __init__(self) -> None:
        self._active_connections: list[WebSocket] = []

    def get_active_connections_number(self) -> int:
        return len(self._active_connections)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        if websocket in self._active_connections:
            self._active_connections.remove(websocket)

    async def broadcast(self, msg_obj: dict) -> None:
        serialized_msg: str = json.dumps(msg_obj)

        for websocket in self._active_connections:
            if websocket.application_state == WebSocketState.CONNECTED:
                try:
                    await websocket.send_text(serialized_msg)

                except Exception as e:
                    logging.error(f"Error sending message: {e}")
