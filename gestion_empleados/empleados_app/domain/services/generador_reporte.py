from typing import List, Dict
from domain.entities.nomina import Nomina

class GeneradorReporte:

    def generar(self, nomina: Nomina) -> Dict:
        reporte = {
            "periodo": {
                "inicio": nomina.fecha_inicio.isoformat(),
                "fin": nomina.fecha_fin.isoformat(),
            },
            "total_pagado": nomina.total_pagado(),
            "pagos": []
        }

        for pago in nomina.pagos:
            reporte["pagos"].append({
                "empleado_dni": pago.empleado_dni,
                "monto_base": pago.monto_base,
                "ajustes": [
                    {"concepto": ajuste.concepto, "monto": ajuste.monto}
                    for ajuste in pago.ajustes
                ],
                "total": pago.calcular_total()
            })

        return reporte