from io import BytesIO
from domain.ports.servicio_reporte import IServicioReporte


class PDFAdapter(IServicioReporte):
    

    def generar(self, nomina):
        buffer = BytesIO()
        # --- aquí iría reportlab, por ahora solo demostrativo ---
        buffer.write(b"%PDF-1.4\n% ... contenido ficticio ...\n")
        return buffer.getvalue()