import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import ASGIHandler, get_asgi_application

import notifications.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "notification_project.settings")

django_asgi_app: ASGIHandler = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(notifications.routing.websocket_urlpatterns),
        ),
    }
)
