from django.urls import URLPattern, path

from chat.consumers import ChatConsumer


websocket_urlpatterns: list[URLPattern] = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]
