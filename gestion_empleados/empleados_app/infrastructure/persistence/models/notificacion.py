from django.db import models


class NotificacionModel(models.Model):
    TIPO_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    empleado = models.ForeignKey('empleados_app.EmpleadoModel', on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    class Meta:
        db_table = 'notificaciones'