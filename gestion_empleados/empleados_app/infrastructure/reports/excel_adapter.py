from io import BytesIO

from empleados_app.domain.ports.generador_reporte import IGeneradorReporte
from empleados_app.domain.entities.empleado import Empleado
from typing import List
import io
import xlsxwriter

class GeneradorReporteExcel(IGeneradorReporte):

    def generar(self, empleados: List[Empleado], formato: str = "excel") -> bytes:
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        headers = ["ID", "Nombre", "DNI", "Email", "Fecha Ingreso", "Tipo", "Salario"]
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        for row, emp in enumerate(empleados, start=1):
            worksheet.write(row, 0, emp.id)
            worksheet.write(row, 1, emp.nombre)
            worksheet.write(row, 2, emp.dni)
            worksheet.write(row, 3, emp.email)
            worksheet.write(row, 4, str(emp.fecha_ingreso))
            worksheet.write(row, 5, emp.tipo_empleado)
            worksheet.write(row, 6, emp.calcular_salario())

        workbook.close()
        output.seek(0)
        return output.read()