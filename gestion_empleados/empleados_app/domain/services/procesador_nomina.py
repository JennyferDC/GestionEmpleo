from datetime import date
from typing import List
from empleados_app.domain.entities.nomina import Pago, Ajuste, Nomina
from empleados_app.domain.services.calculadora_salario import CalculadoraSalario
from empleados_app.domain.ports.repositorio_empleado import IRepositorioEmpleado


class ProcesadorNomina:

    def __init__(self, repositorio_empleado: IRepositorioEmpleado):
        self.repositorio = repositorio_empleado
        self.calculadora = CalculadoraSalario() 

    def procesar_nomina(self, fecha_inicio: date, fecha_fin: date) -> Nomina:
        empleados = self.repositorio.obtener_todos()
        pagos: List[Pago] = []

        for empleado in empleados:
            salario = self.calculadora.calcular(empleado)
            pago = Pago(empleado_dni=empleado.dni, monto_base=salario)
            pagos.append(pago)

        return Nomina(fecha_inicio=fecha_inicio, fecha_fin=fecha_fin, pagos=pagos)