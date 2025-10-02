print("Prueba clientes")
# Módulo de Clientes
# Día 1: Definición inicial

class Cliente:
    def _init_(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.historial_reservas = []

    def _str_(self):
        return f"Cliente[{self.id_cliente}] - {self.nombre} ({self.correo})"
    