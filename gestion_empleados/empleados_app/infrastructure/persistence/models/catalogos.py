from django.db import models


class TipoEmpleadoModel(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tipo_empleado'


class MetodoPagoModel(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'metodo_pago'