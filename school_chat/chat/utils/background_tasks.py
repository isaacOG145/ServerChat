import threading
import time
from datetime import datetime

class NotificationInterceptor:
    def __init__(self):
        self.important_keywords = ['profesor', 'tarea', 'examen', 'importante']
        self.notification_thread = None

    def process(self, message, username):
        """Analiza el mensaje y lanza notificaciones en segundo plano"""
        if self.contains_important_keywords(message):
            self.launch_notification_task(message, username)
        
        return message  # No modifica el mensaje

    def contains_important_keywords(self, message):
        """Detecta palabras importantes"""
        lower_message = message.lower()
        return any(keyword in lower_message for keyword in self.important_keywords)

    def launch_notification_task(self, message, username):
        """Lanza una tarea de notificación en segundo plano"""
        def send_notifications():
            # Simular procesamiento en segundo plano
            time.sleep(1)
            print(f"🔔 Notificación: Mensaje importante de {username}: {message[:50]}...")
            # Aquí podrías integrar con email, push notifications, etc.
        
        self.notification_thread = threading.Thread(target=send_notifications)
        self.notification_thread.daemon = True
        self.notification_thread.start()