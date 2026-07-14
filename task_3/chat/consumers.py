from __future__ import annotations

from typing import Any

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ChatConsumer(AsyncJsonWebsocketConsumer):
    group_name: str = "chat"

    async def connect(self) -> None:
        """Accept a client connection and subscribe it to the chat group."""
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        """Remove a client from the chat group."""
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict[str, Any]) -> None:
        """Receive a chat message and broadcast it with the author's username."""
        user = self.scope["user"]
        if not user.is_authenticated:
            await self.send_json({"error": "auth_required"})
            return

        message = str(content.get("message", "")).strip()
        if not message:
            return

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat.message",
                "username": user.username,
                "message": message,
            },
        )

    async def chat_message(self, event: dict[str, Any]) -> None:
        """Deliver a chat message to a single WebSocket client."""
        await self.send_json(
            {
                "username": event["username"],
                "message": event["message"],
            }
        )
