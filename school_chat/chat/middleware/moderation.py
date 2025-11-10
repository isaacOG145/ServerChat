import re
import threading
from collections import defaultdict

class ModerationInterceptor:
    def __init__(self):
        self.bad_words = ['palabra1', 'palabra2']  # Lista de palabras prohibidas
        self.user_message_count = defaultdict(int)
        self.lock = threading.Lock()

    def process(self, message, username):
        """Modera el mensaje y aplica reglas"""
        # 1. Verificar palabras prohibidas
        if self.contains_bad_words(message):
            return "[MENSAJE MODERADO]"

        # 2. Verificar spam (en hilo seguro)
        with self.lock:
            self.user_message_count[username] += 1
            if self.user_message_count[username] > 10:  # Límite de mensajes
                return "[LÍMITE DE MENSAJES EXCEDIDO]"

        # 3. Limpiar formato excesivo
        cleaned_message = self.clean_excessive_formatting(message)
        
        return cleaned_message

    def contains_bad_words(self, message):
        """Verifica palabras prohibidas usando hilos"""
        lower_message = message.lower()
        return any(bad_word in lower_message for bad_word in self.bad_words)

    def clean_excessive_formatting(self, message):
        """Limpia formato excesivo del mensaje"""
        # Limitar mayúsculas excesivas
        if len(re.findall(r'[A-Z]', message)) > len(message) * 0.7:
            message = message.capitalize()
        
        # Limitar caracteres repetidos
        message = re.sub(r'(.)\1{3,}', r'\1\1', message)
        
        return message