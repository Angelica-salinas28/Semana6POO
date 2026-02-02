# Clase derivada Estudiante
# HEREDA de Persona

from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera

    # POLIMORFISMO: se sobrescribe el método presentarse
    def presentarse(self):
        return f"Hola, soy {self.get_nombre()}, tengo {self.get_edad()} años y estudio {self.carrera}."
