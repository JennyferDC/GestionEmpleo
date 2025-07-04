from ...domain.ports.notificador import INotificador

from empleados_app.domain.entities.notificacion import Notificacion
from empleados_app.infrastructure.notifications.email_adapter import EmailAdapter
from empleados_app.infrastructure.notifications.sms_adapter import SMSAdapter


class NotificadorEmailSMS(INotificador):
    def __init__(self):
        self.email_adapter = EmailAdapter()
        self.sms_adapter = SMSAdapter()

    def enviar(self, notificacion: Notificacion) -> None:
        if notificacion.tipo == "email":
            self.email_adapter.enviar(notificacion.destinatario, notificacion.mensaje)
        elif notificacion.tipo == "sms":
            self.sms_adapter.enviar(notificacion.destinatario, notificacion.mensaje)
        else:
            raise ValueError(f"Tipo de notificación no soportado: {notificacion.tipo}")