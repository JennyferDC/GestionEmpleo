from datetime import date
from typing import List


class Ajuste:
   
    def __init__(self, concepto: str, monto: float):
        self.concepto = concepto
        self.monto = monto


class DetallePago:
   
    def __init__(self, concepto: str, monto: float):
        self.concepto = concepto
        self.monto = monto


class Pago:
    
    def __init__(self, empleado_dni: str, monto_base: float, ajustes: List[Ajuste] = []):
        self.empleado_dni = empleado_dni  # Relación lógica con el empleado
        self.monto_base = monto_base
        self.ajustes = ajustes or []

    def calcular_total(self) -> float:
        total_ajustes = sum(a.monto for a in self.ajustes)
        return self.monto_base + total_ajustes


class Nomina:
   
    def __init__(self, fecha_inicio: date, fecha_fin: date, pagos: List[Pago]):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.pagos = pagos

    def total_pagado(self) -> float:
        return sum(p.calcular_total() for p in self.pagos)