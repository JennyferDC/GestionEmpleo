from abc import ABC, abstractmethod
from domain.entities.nomina import Nomina


class IServicioReporte(ABC):

    @abstractmethod
    def generar(self, nomina: Nomina) -> bytes:
        
        pass