from rest_framework import serializers
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoModel
        fields = [
            "id",
            "nombre",
            "dni",
            "email",
            "fecha_ingreso",
            "tipo_empleado",
            "salario_fijo",
            "salario_hora",
            "horas_trabajadas",
            "tarifa_proyecto",
        ]

class ProcesarNominaSerializer(serializers.Serializer):
    fecha_inicio = serializers.DateField()
    fecha_fin   = serializers.DateField()