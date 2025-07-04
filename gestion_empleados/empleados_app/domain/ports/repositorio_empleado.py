from abc import ABC, abstractmethod
from typing import List
from empleados_app.domain.entities.empleado import Empleado

class IRepositorioEmpleado(ABC):

    @abstractmethod
    def guardar(self, empleado: Empleado) -> None:
        pass

    @abstractmethod
    def obtener_por_id(self, id: int) -> Empleado:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Empleado]:
        pass