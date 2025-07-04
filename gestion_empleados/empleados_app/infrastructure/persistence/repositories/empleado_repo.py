
from empleados_app.domain.entities.empleado import (
    Empleado, 
    EmpleadoTiempoCompleto, 
    EmpleadoMedioTiempo, 
    Contratista
)
from empleados_app.domain.ports.repositorio_empleado import IRepositorioEmpleado
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from typing import List

class RepositorioEmpleado(IRepositorioEmpleado):

    def guardar(self, empleado: Empleado) -> None:
        data = {
            "nombre": empleado.nombre,
            "dni": empleado.dni,
            "email": empleado.email,
            "fecha_ingreso": empleado.fecha_ingreso,
            "tipo": empleado.tipo_empleado,
        }

        if isinstance(empleado, EmpleadoTiempoCompleto):
            data["salario_mensual"] = empleado.salario_mensual
        elif isinstance(empleado, EmpleadoMedioTiempo):
            data["horas_trabajadas"] = empleado.horas_trabajadas
            data["tarifa_hora"] = empleado.tarifa_hora
        elif isinstance(empleado, Contratista):
            data["pago_contrato"] = empleado.pago_contrato

        EmpleadoModel.objects.update_or_create(
            dni=empleado.dni,
            defaults=data
        )

    def obtener_por_id(self, id: int) -> Empleado:
        emp = EmpleadoModel.objects.get(pk=id)
        return self._to_entity(emp)

    def obtener_todos(self) -> List[Empleado]:
        return [self._to_entity(emp) for emp in EmpleadoModel.objects.all()]

    def _to_entity(self, emp: EmpleadoModel) -> Empleado:
        if emp.tipo_empleado == "tiempo_completo":
            return EmpleadoTiempoCompleto(
                id=emp.id, nombre=emp.nombre, dni=emp.dni,
                email=emp.email, fecha_ingreso=emp.fecha_ingreso,
                salario_mensual=emp.salario_mensual
            )
        elif emp.tipo_empleado == "medio_tiempo":
            return EmpleadoMedioTiempo(
                id=emp.id, nombre=emp.nombre, dni=emp.dni,
                email=emp.email, fecha_ingreso=emp.fecha_ingreso,
                horas_trabajadas=emp.horas_trabajadas,
                tarifa_hora=emp.tarifa_hora
            )
        elif emp.tipo_empleado == "contratista":
            return Contratista(
                id=emp.id, nombre=emp.nombre, dni=emp.dni,
                email=emp.email, fecha_ingreso=emp.fecha_ingreso,
                pago_contrato=emp.pago_contrato
            )
        else:
            raise ValueError(f"Tipo de empleado desconocido: {emp.tipo_empleado}")
