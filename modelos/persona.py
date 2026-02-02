# Clase base Persona
# Aquí se aplica ENCAPSULACIÓN usando atributos privados

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre   # atributo privado
        self.__edad = edad       # atributo privado

    # Métodos getter (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (POLIMORFISMO)
    def presentarse(self):
        return f"Hola, soy {self.__nombre} y tengo {self.__edad} años."
