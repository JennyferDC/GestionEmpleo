
from empleados_app.domain.entities.notificacion import Notificacion 

from empleados_app.domain.ports.repositorio_empleado import IRepositorioEmpleado
from empleados_app.domain.ports.repositorio_pago import IRepositorioPago
from empleados_app.domain.ports.notificador import INotificador
from empleados_app.domain.services.calculadora_salario import CalculadoraSalario
from empleados_app.domain.entities.pago import Pago
from datetime import date

class ProcesadorPagos:

    def __init__(
        self,
        repo_empleado: IRepositorioEmpleado,
        repo_pago: IRepositorioPago,
        notificador: INotificador,
    ):
        self.repo_empleado = repo_empleado
        self.repo_pago = repo_pago
        self.notificador = notificador
        self.calculadora = CalculadoraSalario()

    def procesar(self):
        empleados = self.repo_empleado.obtener_todos()

        for empleado in empleados:
            salario = self.calculadora.calcular(empleado)

            pago = Pago(
                empleado_id=empleado.id,
                monto_pagado=salario,
                fecha_pago=date.today(),
            )
            self.repo_pago.guardar(pago)

            mensaje = f"Se ha procesado el pago de {salario:.2f} para {empleado.nombre}"
            notificacion = Notificacion(
                destinatario=empleado.email,
                mensaje=mensaje,
                tipo="email",
            )
            self.notificador.enviar(notificacion)   # ✅