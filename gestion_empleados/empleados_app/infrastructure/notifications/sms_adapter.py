from ...domain.ports.notificador import IServicioNotificacion

class SMSAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str):
        
        print(f"[SMS] Enviando a {destinatario}: {mensaje}")