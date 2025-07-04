from io import BytesIO
from empleados_app.domain.ports.generador_reporte import IGeneradorReporte

class PDFAdapter(IGeneradorReporte):

    def generar(self, nomina) -> bytes:
        buffer = BytesIO()
        # Aquí iría el uso de reportlab o similar para generar el PDF
        buffer.write(b"%PDF-1.4\n% ... contenido ficticio ...\n")
        return buffer.getvalue()