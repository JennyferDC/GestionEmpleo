from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from empleados_app.infrastructure.persistence.models.empleado import EmpleadoModel
from empleados_app.api.serializers import EmpleadoSerializer

from empleados_app.domain.services.generador_reporte import GeneradorReporteEmpleados
from empleados_app.domain.services.procesador_pagos import ProcesadorPagos
from empleados_app.infrastructure.persistence.repositories.empleado_repo import RepositorioEmpleado
from empleados_app.infrastructure.persistence.repositories.pago_repo import RepositorioPago

from empleados_app.infrastructure.notifications.notificador_email_sms import NotificadorEmailSMS
from empleados_app.infrastructure.reports.excel_adapter import GeneradorReporteExcel
from empleados_app.infrastructure.reports.pdf_adapter import PDFAdapter

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = EmpleadoModel.objects.all()
    serializer_class = EmpleadoSerializer

    @action(detail=False, methods=["get"])
    def generar_reporte(self, request):
        formato = request.query_params.get("formato", "pdf")  # opcional: pdf, excel, json

        repo = RepositorioEmpleado()

        if formato == "pdf":
            generador = PDFAdapter()
            content_type = "application/pdf"
            filename = "reporte_empleados.pdf"
        elif formato == "excel":
            generador = GeneradorReporteExcel()
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            filename = "reporte_empleados.xlsx"
        else:
            return Response({"error": "Formato no soportado"}, status=400)

        servicio = GeneradorReporteEmpleados(repo, generador)
        contenido = servicio.generar(formato=formato)

        return Response(
            contenido,
            content_type=content_type,
            headers={"Content-Disposition": f"attachment; filename={filename}"},
        )
    
    @action(detail=False, methods=["post"])
    def procesar_pagos(self, request):
    
        repo_empleado = RepositorioEmpleado()
        repo_pago = RepositorioPago()
        notificador = NotificadorEmailSMS()  # Usa tus adapters internos

        servicio = ProcesadorPagos(repo_empleado, repo_pago, notificador)
        servicio.procesar()

        return Response({"mensaje": "Pagos procesados correctamente"}, status=200)

