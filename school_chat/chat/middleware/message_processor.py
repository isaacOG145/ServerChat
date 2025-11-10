import threading
import time
from datetime import datetime

class MessageProcessor:
    def __init__(self):
        self.interceptors = []
        self.setup_interceptors()

    def setup_interceptors(self):
        """Registra todos los interceptores"""
        from .moderation import ModerationInterceptor
        from ..utils.background_tasks import NotificationInterceptor
        
        self.interceptors.append(ModerationInterceptor())
        self.interceptors.append(NotificationInterceptor())

    def process_message(self, message, username):
        """Ejecuta todos los interceptores en el mensaje"""
        processed_message = message
        
        for interceptor in self.interceptors:
            try:
                # Cada interceptor puede modificar el mensaje
                result = interceptor.process(processed_message, username)
                if result is not None:
                    processed_message = result
                    
                # Si algún interceptor devuelve False, se cancela el mensaje
                if result is False:
                    return None
                    
            except Exception as e:
                print(f"Interceptor error: {e}")
                continue
        
        return processed_message