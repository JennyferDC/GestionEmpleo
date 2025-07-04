from abc import ABC, abstractmethod
from typing import List
from empleados_app.domain.entities.empleado import EmpleadoBase


class IRepositorioEmpleado(ABC):

    @abstractmethod
    def obtener_todos(self) -> List[EmpleadoBase]:
        pass

    @abstractmethod
    def obtener_por_dni(self, dni: str) -> EmpleadoBase:
        pass