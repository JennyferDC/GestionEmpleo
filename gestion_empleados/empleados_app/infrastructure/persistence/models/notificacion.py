from django.db import models
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel

class NotificacionModel(models.Model):

    TIPO_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]

    empleado = models.ForeignKey(
        EmpleadoModel,
        on_delete=models.CASCADE,
        related_name='notificaciones'
    )
    mensaje = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.upper()} a {self.empleado.email} el {self.fecha_envio.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        db_table = 'notificaciones'
        ordering = ['-fecha_envio']