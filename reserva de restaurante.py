class Reserva:
    def __init__(self, fecha, hora, personas, requisitos_especiales):
        self.fecha = fecha
        self.hora = hora
        self.personas = personas
        self.requisitos_especiales = requisitos_especiales

class Restaurante:
    def __init__(self):
        self.reservas = []

    def verificar_disponibilidad(self, fecha, hora, personas):
        # Aquí iría el código para verificar la disponibilidad

     def registrar_reserva(self, reserva):
   # Aquí iría el código para registrar la reserva

       def confirmar_reserva(self, reserva):
        # Aquí iría el código para confirmar la reserva