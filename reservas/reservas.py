# Módulo de Reservas
# Día 1: Definición inicial

class Reserva:
    def _init_(self, id_reserva, cliente, habitacion, fecha_inicio, fecha_fin):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def _str_(self):
        return f"Reserva[{self.id_reserva}] - Cliente: {self.cliente.nombre}, Habitación: {self.habitacion.id_habitacion}, Fechas: {self.fecha_inicio} a {self.fecha_fin}"