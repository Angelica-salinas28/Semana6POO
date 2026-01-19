from modelos.dispositivo import Dispositivo

# Clase Computadora hereda de Dispositivo
class Computadora(Dispositivo):
    def __init__(self, marca, modelo, ram):
        super().__init__(marca, modelo)  # herencia
        self.ram = ram

    # Polimorfismo: sobrescribe el método descripcion
    def descripcion(self):
        return f"Computadora marca {self._marca}, modelo {self._modelo}, RAM {self.ram}GB"
    
