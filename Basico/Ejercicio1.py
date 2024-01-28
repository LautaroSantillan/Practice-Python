class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El alumno {self.nombre} esta estudiando...")
# --------- #
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
grado = input("Ingrese en que grado/año esta: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
        DATOS DEL ESTUDIANTE: 
        Nombre: {estudiante.nombre}
        Edad: {estudiante.edad}
        Grado/Año: {estudiante.grado}
      """)
# --------- #
while True:
    estudiar = input("Ingrese 'estudiar': ")
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()
        break
    
    