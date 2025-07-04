from abc import ABC, abstractmethod
from datetime import date


class EmpleadoBase(ABC):

    def __init__(self, nombre: str, dni: str, email: str, fecha_ingreso: date, tipo_empleado: str):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.fecha_ingreso = fecha_ingreso
        self.tipo_empleado = tipo_empleado

    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class EmpleadoTiempoCompleto(EmpleadoBase):

    def __init__(self, nombre, dni, email, fecha_ingreso, salario_mensual: float):
        super().__init__(nombre, dni, email, fecha_ingreso, "Tiempo Completo")
        self.salario_mensual = salario_mensual

    def calcular_salario(self) -> float:
        return self.salario_mensual


class EmpleadoMedioTiempo(EmpleadoBase):

    def __init__(self, nombre, dni, email, fecha_ingreso, salario_hora: float, horas_trabajadas: float):
        super().__init__(nombre, dni, email, fecha_ingreso, "Medio Tiempo")
        self.salario_hora = salario_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self) -> float:
        return self.salario_hora * self.horas_trabajadas


class Contratista(EmpleadoBase):

    def __init__(self, nombre, dni, email, fecha_ingreso, tarifa_proyecto: float):
        super().__init__(nombre, dni, email, fecha_ingreso, "Contratista")
        self.tarifa_proyecto = tarifa_proyecto

    def calcular_salario(self) -> float:
        return self.tarifa_proyecto