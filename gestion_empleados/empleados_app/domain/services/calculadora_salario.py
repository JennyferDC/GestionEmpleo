from empleados_app.domain.entities.empleado import Empleado

class CalculadoraSalario:
    
    def calcular(self, empleado: Empleado) -> float:
        return empleado.calcular_salario()