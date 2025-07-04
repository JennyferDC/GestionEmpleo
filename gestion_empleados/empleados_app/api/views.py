from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from empleados_app.api.serializers import EmpleadoSerializer

# Servicios del dominio + infraestructura
from empleados_app.domain.services.generador_reporte import GeneradorReporteEmpleados
from empleados_app.infrastructure.reports.excel_adapter import IGeneradorReporte
from empleados_app.infrastructure.persistence.repositories.empleado_repo import RepositorioEmpleado

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoModel.objects.all()
    serializer_class = EmpleadoSerializer

    @action(detail=False, methods=["get"])
    def generar_reporte(self, request):
        formato = request.query_params.get("formato", "pdf")  # opcional: pdf, excel, json

        repo = RepositorioEmpleado()

        if formato == "pdf":
            generador = IGeneradorReporte()
            content_type = "application/pdf"
            filename = "reporte_empleados.pdf"
        else:
            return Response({"error": "Formato no soportado"}, status=400)

        servicio = GeneradorReporteEmpleados(repo, generador)
        contenido = servicio.generar(formato=formato)

        return Response(
            contenido,
            content_type=content_type,
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )