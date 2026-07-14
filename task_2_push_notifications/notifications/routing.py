from django.urls import URLPattern, path

from notifications.consumers import PushNotificationConsumer


websocket_urlpatterns: list[URLPattern] = [
    path("ws/notifications/", PushNotificationConsumer.as_asgi()),
]
