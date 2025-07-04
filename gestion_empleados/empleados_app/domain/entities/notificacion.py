class Notificacion:
    def __init__(self, destinatario: str, mensaje: str, tipo: str):
        self.destinatario = destinatario
        self.mensaje = mensaje
        self.tipo = tipo  # ej: 'email', 'sms'

