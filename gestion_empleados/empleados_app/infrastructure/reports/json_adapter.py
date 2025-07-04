import json
from domain.ports.servicio_reporte import IServicioReporte


class JSONAdapter(IServicioReporte):

    def generar(self, nomina):
        estructura = {
            "inicio": nomina.fecha_inicio.isoformat(),
            "fin": nomina.fecha_fin.isoformat(),
            "total": nomina.total_pagado(),
            "pagos": [
                {
                    "dni": p.empleado_dni,
                    "base": p.monto_base,
                    "ajustes": [{ "c": a.concepto, "m": a.monto } for a in p.ajustes],
                    "total": p.calcular_total(),
                }
                for p in nomina.pagos
            ],
        }
        return json.dumps(estructura, ensure_ascii=False).encode()