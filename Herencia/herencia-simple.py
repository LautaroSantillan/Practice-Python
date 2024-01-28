class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"Hola {self.nombre}! Cómo estas?")
#Clase Hija
class Empleado(Persona):
        def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
            super().__init__(nombre, edad, nacionalidad)
            self.trabajo = trabajo
            self.salario = salario

class Estudiante(Persona):
        def __init__(self, nombre, edad, nacionalidad, universidad, nota):
            super().__init__(nombre, edad, nacionalidad)
            self.universidad = universidad
            self.nota = nota
# --------- #
lautaro = Empleado("Lautaro", 20, "argentino", "programador", 100)
lautaro.hablar()
