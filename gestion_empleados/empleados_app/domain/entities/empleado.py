from abc import ABC, abstractmethod
from datetime import date

class Empleado(ABC):
    def __init__(self, id: int, nombre: str, dni: str, email: str, fecha_ingreso: date, tipo_empleado: str):
        self.id = id
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.fecha_ingreso = fecha_ingreso
        self.tipo_empleado = tipo_empleado

    @abstractmethod
    def calcular_salario(self) -> float:
        pass


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, id: int, nombre: str, dni: str, email: str, fecha_ingreso: date, salario_mensual: float):
        super().__init__(id, nombre, dni, email, fecha_ingreso, tipo_empleado="tiempo_completo")
        self.salario_mensual = salario_mensual

    def calcular_salario(self) -> float:
        return self.salario_mensual


class EmpleadoMedioTiempo(Empleado):
    def __init__(self, id: int, nombre: str, dni: str, email: str, fecha_ingreso: date, horas_trabajadas: int, tarifa_hora: float):
        super().__init__(id, nombre, dni, email, fecha_ingreso, tipo_empleado="medio_tiempo")
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario(self) -> float:
        return self.horas_trabajadas * self.tarifa_hora


class Contratista(Empleado):
    def __init__(self, id: int, nombre: str, dni: str, email: str, fecha_ingreso: date, pago_contrato: float):
        super().__init__(id, nombre, dni, email, fecha_ingreso, tipo_empleado="contratista")
        self.pago_contrato = pago_contrato

    def calcular_salario(self) -> float:
        return self.pago_contrato
