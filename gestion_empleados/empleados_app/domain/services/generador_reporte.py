from empleados_app.domain.ports.repositorio_empleado import IRepositorioEmpleado
from empleados_app.domain.ports.generador_reporte import IGeneradorReporte

class GeneradorReporteEmpleados:

    def __init__(self, repo_empleado: IRepositorioEmpleado, generador: IGeneradorReporte):
        self.repo_empleado = repo_empleado
        self.generador = generador

    def generar(self, formato: str) -> bytes:
        empleados = self.repo_empleado.obtener_todos()
        return self.generador.generar(empleados, formato)