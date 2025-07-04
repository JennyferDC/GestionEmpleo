from io import BytesIO
from domain.ports.servicio_reporte import IServicioReporte


class ExcelAdapter(IServicioReporte):
   

    def generar(self, nomina):
        buffer = BytesIO()
        # Aquí crearías el workbook; placeholder:
        buffer.write(b"PK\x03\x04 ... firma zip de XLSX ...")
        return buffer.getvalue()