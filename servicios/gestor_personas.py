# Clase que gestiona personas y estudiantes
# Separación de responsabilidades (buena práctica)

class GestorPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def mostrar_presentaciones(self):
        for persona in self.personas:
            print(persona.presentarse())  # POLIMORFISMO en acción
