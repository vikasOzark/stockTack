"""
ASGI config for core_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

from channels.routing import ProtocolTypeRouter, URLRouter
import os
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from stocks import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_site.settings')
get_asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application,
    # Just HTTP for now. (We can add other protocols later.)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
})