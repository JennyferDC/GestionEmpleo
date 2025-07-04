from empleados_app.domain.ports.repositorio_pago import IRepositorioPago
from empleados_app.domain.entities.pago import Pago
from empleados_app.infrastructure.persistence.models.pago import PagoModel
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from typing import List

class RepositorioPago(IRepositorioPago):

    def guardar(self, pago: Pago) -> None:
        empleado = EmpleadoModel.objects.get(pk=pago.empleado_id)
        PagoModel.objects.create(
            empleado=empleado,
            monto_pagado=pago.monto_pagado,
            fecha_pago=pago.fecha_pago
        )

    def obtener_por_empleado(self, empleado_id: int) -> List[Pago]:
        pagos = PagoModel.objects.filter(empleado__id=empleado_id)
        return [self._to_entity(pag) for pag in pagos]

    def obtener_todos(self) -> List[Pago]:
        pagos = PagoModel.objects.all()
        return [self._to_entity(pag) for pag in pagos]

    def _to_entity(self, pago_model: PagoModel) -> Pago:
        return Pago(
            empleado_id=pago_model.empleado.id,
            monto_pagado=pago_model.monto_pagado,
            fecha_pago=pago_model.fecha_pago
        )