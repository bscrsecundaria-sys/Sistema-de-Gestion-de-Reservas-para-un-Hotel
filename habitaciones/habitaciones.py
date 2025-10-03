# Módulo de Habitaciones
# Día 1: Definición inicial

class Habitacion:
    def __init__(self, id_habitacion, tipo, tarifa, estado="disponible"):
        self.id_habitacion = id_habitacion
        self.tipo = tipo
        self.tarifa = tarifa
        self.estado = estado  # disponible, ocupada, mantenimiento

    def __str__(self):
        return f"Habitación[{self.id_habitacion}] - {self.tipo} (${self.tarifa}) [{self.estado}]"
