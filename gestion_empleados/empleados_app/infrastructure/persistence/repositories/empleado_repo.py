from empleados_app.domain.ports.repositorio_empleado import IRepositorioEmpleado
from empleados_app.domain.entities.empleado import (
    EmpleadoTiempoCompleto,
    EmpleadoMedioTiempo,
    Contratista
)
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
class RepositorioEmpleado(IRepositorioEmpleado):

    def obtener_todos(self):
        empleados = EmpleadoModel.objects.all()
        return [self._convertir_a_entidad(emp) for emp in empleados]

    def obtener_por_dni(self, dni: str):
        try:
            emp = EmpleadoModel.objects.get(dni=dni)
            return self._convertir_a_entidad(emp)
        except EmpleadoModel.DoesNotExist:
            raise ValueError(f"Empleado con DNI {dni} no encontrado")

    def _convertir_a_entidad(self, emp: EmpleadoModel):
        tipo = emp.tipo_empleado.lower()

        if tipo == "tiempo completo":
            return EmpleadoTiempoCompleto(
                nombre=emp.nombre,
                dni=emp.dni,
                email=emp.email,
                fecha_ingreso=emp.fecha_ingreso,
                salario_mensual=emp.salario_fijo
            )
        elif tipo == "medio tiempo":
            return EmpleadoMedioTiempo(
                nombre=emp.nombre,
                dni=emp.dni,
                email=emp.email,
                fecha_ingreso=emp.fecha_ingreso,
                salario_hora=emp.salario_hora,
                horas_trabajadas=emp.horas_trabajadas or 0
            )
        elif tipo == "contratista":
            return Contratista(
                nombre=emp.nombre,
                dni=emp.dni,
                email=emp.email,
                fecha_ingreso=emp.fecha_ingreso,
                tarifa_proyecto=emp.tarifa_proyecto
            )
        else:
            raise ValueError(f"Tipo de empleado no reconocido: {emp.tipo_empleado}")