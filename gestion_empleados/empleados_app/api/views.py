from rest_framework import viewsets
from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from empleados_app.api.serializers import EmpleadoSerializer

from rest_framework import viewsets, status               
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import date

from empleados_app.api.serializers import (
    EmpleadoSerializer,
    ProcesarNominaSerializer,           
)

from empleados_app.domain.services.procesador_nomina import ProcesadorNomina
from empleados_app.infrastructure.persistence.repositories.empleado_repo import RepositorioEmpleado


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoModel.objects.all()
    serializer_class = EmpleadoSerializer

    @action(detail=False, methods=["post"], url_path="procesar_nomina")
    def procesar_nomina(self, request):
        serializer = ProcesarNominaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        fecha_inicio = serializer.validated_data["fecha_inicio"]
        fecha_fin    = serializer.validated_data["fecha_fin"]

        procesador = ProcesadorNomina(RepositorioEmpleado())
        nomina = procesador.procesar_nomina(fecha_inicio, fecha_fin)

        data = {
            "fecha_inicio": str(nomina.fecha_inicio),
            "fecha_fin": str(nomina.fecha_fin),
            "pagos": [
                {"empleado_dni": p.empleado_dni, "monto_base": p.monto_base}
                for p in nomina.pagos
            ],
        }
        return Response(data)