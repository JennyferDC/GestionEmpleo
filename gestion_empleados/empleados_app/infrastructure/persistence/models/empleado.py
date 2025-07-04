from django.db import models

class EmpleadoModel(models.Model):

    TIPO_CHOICES = [
        ('Tiempo Completo', 'Tiempo Completo'),
        ('Medio Tiempo', 'Medio Tiempo'),
        ('Contratista', 'Contratista'),
    ]

    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    fecha_ingreso = models.DateField()
    tipo_empleado = models.CharField(max_length=20, choices=TIPO_CHOICES)

    # Campos opcionales según el tipo
    salario_fijo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salario_hora = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    horas_trabajadas = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    tarifa_proyecto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'empleados'