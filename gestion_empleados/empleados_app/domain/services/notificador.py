from domain.ports.servicio_notificacion import IServicioNotificacion
from domain.entities.nomina import Nomina


class Notificador:

    def __init__(self, servicio_notificacion: IServicioNotificacion):
        self.servicio = servicio_notificacion

    def notificar_nomina(self, nomina: Nomina):
        for pago in nomina.pagos:
            mensaje = (
                f"Hola! Tu pago ha sido procesado. "
                f"Total: {pago.calcular_total():.2f} soles."
            )
            self.servicio.enviar(pago.empleado_dni, mensaje)
