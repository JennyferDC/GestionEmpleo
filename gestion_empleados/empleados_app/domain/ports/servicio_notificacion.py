from abc import ABC, abstractmethod

class IServicioNotificacion(ABC):

    @abstractmethod
    def enviar(self, empleado_dni: str, mensaje: str):

        pass