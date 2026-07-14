from __future__ import annotations

from typing import Any

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class PushNotificationConsumer(AsyncJsonWebsocketConsumer):
    group_name: str = "push_notifications"

    async def connect(self) -> None:
        """Accept a client connection and subscribe it to notifications."""
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        """Remove a client from the notifications group."""
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive_json(self, content: dict[str, Any]) -> None:
        """Receive a message from one client and broadcast it to everyone."""
        message = str(content.get("message", "")).strip()
        if not message:
            return

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "push.notification",
                "message": message,
            },
        )

    async def push_notification(self, event: dict[str, Any]) -> None:
        """Deliver a push notification to a single WebSocket client."""
        await self.send_json({"message": event["message"]})
