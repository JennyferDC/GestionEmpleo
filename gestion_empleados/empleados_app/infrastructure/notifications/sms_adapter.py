from domain.ports.servicio_notificacion import IServicioNotificacion


class SMSAdapter(IServicioNotificacion):

    def enviar(self, destinatario: str, mensaje: str):
        # Aquí podrías conectar a Twilio, Nexmo, etc.
        print(f"[SMS] Enviando a {destinatario}: {mensaje}")