from django.urls import URLPattern, path

from counter.consumers import OnlineUsersConsumer


websocket_urlpatterns: list[URLPattern] = [
    path("ws/online/", OnlineUsersConsumer.as_asgi()),
]
