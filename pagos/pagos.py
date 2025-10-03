# Módulo de Pagos
# Día 1: Definición inicial

class Pago:
    def _init_(self, id_pago, monto, metodo):
        self.id_pago = id_pago
        self.monto = monto
        self.metodo = metodo  # tarjeta, efectivo, etc.
        self.validado = False

    def _str_(self):
        return f"Pago[{self.id_pago}] - ${self.monto} vía {self.metodo} - Validado: {self.validado}"