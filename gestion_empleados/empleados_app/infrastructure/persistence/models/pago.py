from django.db import models
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel

class PagoModel(models.Model):
    empleado = models.ForeignKey('EmpleadoModel', on_delete=models.CASCADE, related_name='pagos')
    monto_pagado = models.FloatField()
    fecha_pago = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.monto_pagado} a {self.empleado.nombre} el {self.fecha_pago}"

    class Meta:
        db_table = 'pagos'
        ordering = ['-fecha_pago']