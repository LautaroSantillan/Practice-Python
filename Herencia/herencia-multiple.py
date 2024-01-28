class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def saludo(self):
        print(f"Hola {self.nombre}! Cómo estas?")
# -------- #
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar(self):
        return f"Mi habilidad es: {self.habilidad}"
# Clase Hija que hereda de otras dos clases
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        print(f"Hola! Soy {self.nombre}\n{self.mostrar()} y trabajo en {self.empresa}")
# -------- #
lautaro = EmpleadoArtista("Lautaro", 20, "argentino", "programar", 100, "HelloWorld")
lautaro.presentarse()
# -------- #
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
instancia = isinstance(lautaro, Persona)
print(instancia)