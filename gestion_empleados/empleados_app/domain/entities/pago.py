from datetime import date

class Pago:
    def __init__(self, empleado_id: int, monto_pagado: float, fecha_pago: date):
        self.empleado_id = empleado_id
        self.monto_pagado = monto_pagado
        self.fecha_pago = fecha_pago