class CalculadoraSalario:

    def calcular(self, empleado) -> float:
        if not hasattr(empleado, "calcular_salario"):
            raise TypeError("El objeto no implementa el método calcular_salario()")
        return empleado.calcular_salario()