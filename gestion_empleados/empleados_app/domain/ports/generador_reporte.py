from abc import ABC, abstractmethod
from empleados_app.domain.entities.empleado import Empleado
from typing import List

class IGeneradorReporte(ABC):
    
    @abstractmethod
    def generar(self, empleados: List[Empleado], formato: str) -> bytes:
        
        pass
    