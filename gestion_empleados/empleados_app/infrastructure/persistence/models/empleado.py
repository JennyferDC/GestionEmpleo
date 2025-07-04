from django.db import models


class EmpleadoModel(models.Model):
    TIPO_CHOICES = [
        ('tiempo_completo', 'tiempo_completo'),
        ('medio_tiempo', 'medio_tiempo'),
        ('contratista', 'contratista'),
    ]

    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    fecha_ingreso = models.DateField()
    tipo_empleado = models.CharField(max_length=20, choices=TIPO_CHOICES)
        

    salario_mensual = models.FloatField(null=True, blank=True)
    horas_trabajadas = models.IntegerField(null=True, blank=True)
    tarifa_hora = models.FloatField(null=True, blank=True)
    pago_contrato = models.FloatField(null=True, blank=True)

    
    def __str__(self):
        return f"{self.nombre} ({self.tipo_empleado})"
    
    class Meta:
        db_table = 'empleados'