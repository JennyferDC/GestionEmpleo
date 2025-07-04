from empleados_app.domain.services.generador_reporte import GeneradorReporteEmpleados
from empleados_app.domain.services.procesador_pagos import ProcesadorPagos
from empleados_app.infrastructure.persistence.repositories.empleado_repo import RepositorioEmpleado
from empleados_app.infrastructure.persistence.repositories.pago_repo import RepositorioPago
from empleados_app.infrastructure.notifications.notificador_email_sms import NotificadorEmailSMS
from empleados_app.infrastructure.reports.pdf_adapter import PDFAdapter
from empleados_app.infrastructure.reports.excel_adapter import GeneradorReporteExcel

class EmpleadoService:
    def generar_reporte_empleados(self, formato="pdf"):
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
            raise ValueError("Formato no soportado")

        servicio = GeneradorReporteEmpleados(repo, generador)
        contenido = servicio.generar(formato=formato)

        return contenido, content_type, filename

    def procesar_pagos(self):
        repo_empleado = RepositorioEmpleado()
        repo_pago = RepositorioPago()
        notificador = NotificadorEmailSMS()

        servicio = ProcesadorPagos(repo_empleado, repo_pago, notificador)
        servicio.procesar()