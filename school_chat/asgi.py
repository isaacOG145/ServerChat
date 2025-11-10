import os
import django
from django.core.asgi import get_asgi_application

# Configurar Django PRIMERO
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_chat.settings')
django.setup()

# Luego importar Channels
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Importar las rutas de WebSocket
try:
    from school_chat.chat.routing import websocket_urlpatterns
    print("WebSocket routes cargadas correctamente")
except ImportError as e:
    print(f"Error cargando WebSocket routes: {e}")
    websocket_urlpatterns = []

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})