from __future__ import annotations

from typing import Any

from channels.generic.websocket import AsyncJsonWebsocketConsumer


class OnlineUsersConsumer(AsyncJsonWebsocketConsumer):
    group_name: str = "online_users"
    online_users_count: int = 0

    async def connect(self) -> None:
        """Accept a client connection and increment the online counter."""
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        OnlineUsersConsumer.online_users_count += 1
        await self.broadcast_count()

    async def disconnect(self, close_code: int) -> None:
        """Remove a client connection and decrement the online counter."""
        OnlineUsersConsumer.online_users_count = max(
            0,
            OnlineUsersConsumer.online_users_count - 1,
        )
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.broadcast_count()

    async def broadcast_count(self) -> None:
        """Send the current online count to all subscribed clients."""
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "online.count",
                "online": OnlineUsersConsumer.online_users_count,
            },
        )

    async def online_count(self, event: dict[str, Any]) -> None:
        """Deliver the online count update to a single WebSocket client."""
        await self.send_json({"online": event["online"]})
