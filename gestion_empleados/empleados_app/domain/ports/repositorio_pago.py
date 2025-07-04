from abc import ABC, abstractmethod
from empleados_app.domain.entities.pago import Pago
from typing import List

class IRepositorioPago(ABC):

    @abstractmethod
    def guardar(self, pago: Pago) -> None:
        pass

    @abstractmethod
    def obtener_por_empleado(self, empleado_id: int) -> List[Pago]:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Pago]:
        pass