from ...domain.ports.notificador import IServicioNotificacion

class EmailAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str) -> None:
       
        print(f"[EMAIL] Enviando a {destinatario}: {mensaje}")

