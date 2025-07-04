from django.db import models


class NominaModel(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    total_pagado = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = 'nominas'


class PagoModel(models.Model):
    nomina = models.ForeignKey(NominaModel, on_delete=models.CASCADE, related_name='pagos')
    empleado = models.ForeignKey('empleados_app.EmpleadoModel', on_delete=models.CASCADE)
    monto_base = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'pagos'


class AjusteModel(models.Model):
    pago = models.ForeignKey(PagoModel, on_delete=models.CASCADE, related_name='ajustes')
    concepto = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'ajustes'