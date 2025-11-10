import os
import sys

# Agregar el directorio raíz al path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_chat.settings')
django.setup()

try:
    from school_chat.chat.routing import websocket_urlpatterns
    print(f"✅ WebSocket patterns cargadas: {len(websocket_urlpatterns)} rutas")
    for pattern in websocket_urlpatterns:
        print(f"   - {pattern.pattern}")
except Exception as e:
    print(f"❌ Error cargando WebSocket routes: {e}")
    import traceback
    traceback.print_exc()