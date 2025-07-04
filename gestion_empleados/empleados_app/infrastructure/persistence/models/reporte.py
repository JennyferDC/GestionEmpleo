from django.db import models


class ReporteModel(models.Model):
    TIPO_CHOICES = [
        ('PDF', 'PDF'),
        ('Excel', 'Excel'),
        ('JSON', 'JSON'),
    ]

    empleado = models.ForeignKey('empleados_app.EmpleadoModel', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    class Meta:
        db_table = 'reportes'