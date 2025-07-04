from domain.ports.servicio_notificacion import IServicioNotificacion


class EmailAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str):
        # Aquí podrías integrar con smtplib, SendGrid, etc.
        print(f"[EMAIL] Enviando a {destinatario}: {mensaje}")