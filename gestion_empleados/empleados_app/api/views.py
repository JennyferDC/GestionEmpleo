from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from empleados_app.api.serializers import EmpleadoSerializer
from empleados_app.domain.services.empleado_service import EmpleadoService

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoModel.objects.all()
    serializer_class = EmpleadoSerializer
    

    @action(detail=False, methods=["get"])
    def generar_reporte(self, request):
        formato = request.query_params.get("formato", "pdf")
        service = EmpleadoService()

        try:
            contenido, content_type, filename = service.generar_reporte_empleados(formato)
            return Response(
                contenido,
                content_type=content_type,
                headers={"Content-Disposition": f"attachment; filename={filename}"},
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=400)

    
    @action(detail=False, methods=["post"])
    def procesar_pagos(self, request):
        service = EmpleadoService()
        service.procesar_pagos()
        return Response({"mensaje": "Pagos procesados correctamente"}, status=200)

