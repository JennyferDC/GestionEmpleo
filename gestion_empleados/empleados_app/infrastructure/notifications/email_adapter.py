from gestion_empleados.empleados_app.domain.ports.notificador import IServicioNotificacion


class EmailAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str):
        # Aquí podrías integrar con smtplib, SendGrid, etc.
        print(f"[EMAIL] Enviando a {destinatario}: {mensaje}")