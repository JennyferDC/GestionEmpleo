from abc import ABC, abstractmethod
from empleados_app.domain.entities.notificacion import Notificacion


class INotificador(ABC):

    @abstractmethod
    def enviar(self, notificacion: Notificacion) -> None:
        pass