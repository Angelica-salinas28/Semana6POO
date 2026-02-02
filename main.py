# Archivo principal que ejecuta el programa

from modelos.persona import Persona
from modelos.estudiante import Estudiante
from servicios.gestor_personas import GestorPersonas

def main():
    # Crear instancias
    persona1 = Persona("Carlos", 40)
    estudiante1 = Estudiante("Ana", 20, "Ingeniería en Sistemas")

    # Gestor del sistema
    gestor = GestorPersonas()
    gestor.agregar_persona(persona1)
    gestor.agregar_persona(estudiante1)

    # Mostrar resultados
    gestor.mostrar_presentaciones()

# Punto de entrada del programa
if __name__ == "__main__":
    main()
