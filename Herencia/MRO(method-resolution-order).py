class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    pass
        
class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B, C):
    pass

class E(B, C):
    def hablar(self):
        print("Hola desde E")

class F(D, A):
    pass
#Funciona en forma de ramas (Arboles - Mat. Discreta)
f = F()
f.hablar()
print(F.mro())
