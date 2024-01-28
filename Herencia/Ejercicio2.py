class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")
# --------- #
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrarGrado(self):
        print(f"Grado/Año: {self.grado}")
# --------- #
estudiante = Estudiante("Lautaro", 20, 3)
estudiante.mostrar()
estudiante.mostrarGrado()
# ---- OTRO EJERCICIO ----- #
class Animal:
    def comer(self):
        print("El animal esta comiendo...")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando...")        

class Ave(Animal):
    def volar(self):
        print("El animal está volando...")    
        
class Murcielago(Mamifero, Ave):
    pass
# --------- #
murcielago = Murcielago()

murcielago.comer()
murcielago.amamantar()
murcielago.volar()