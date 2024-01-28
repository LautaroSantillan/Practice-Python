class Celular:
    #Método Constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #Métodos
    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.modelo}")
        
    def cortar(self):
        print(f"Cortaste un llamado desde un: {self.modelo}")
# --------- #
celular1 = Celular("Sansumg", "S23", "45MP")
celular2 = Celular("Apple", "15 Pro", "96MP")

print(celular1.modelo)
print(celular2.modelo)
# --------- #
celular1.llamar()
celular2.cortar()