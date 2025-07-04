from gestion_empleados.empleados_app.domain.ports.notificador import IServicioNotificacion


class SMSAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str):
        # Aquí podrías conectar a Twilio, Nexmo, etc.
        print(f"[SMS] Enviando a {destinatario}: {mensaje}")