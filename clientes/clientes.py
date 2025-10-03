# Módulo de Clientes
# Día 1: Definición inicial

class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.historial_reservas = []

    def __str__(self):
        return f"Cliente[{self.id_cliente}] - {self.nombre} ({self.correo})"