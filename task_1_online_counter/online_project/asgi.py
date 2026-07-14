import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import ASGIHandler, get_asgi_application

import counter.routing


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "online_project.settings")

django_asgi_app: ASGIHandler = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(counter.routing.websocket_urlpatterns),
        ),
    }
)
