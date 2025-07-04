from django.db import models


class SalarioBaseModel(models.Model):

    TIPO_CHOICES = [
        ('Fijo', 'Fijo'),
        ('Variable', 'Variable'),
    ]

    empleado = models.ForeignKey('empleados_app.EmpleadoModel', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    class Meta:
        db_table = 'salarios_base'