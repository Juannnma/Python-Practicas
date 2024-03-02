class Animales():
    def __init__(self,mensaje):
        self.mensaje=mensaje
    def hablar(self):
        print(self.mensaje)
class Perro(Animales):
    def hablar(self):
        print("Yo no hablo!")
class Pez(Animales):
    def hablar(self):
        print("Yo nado")

perro=Perro("Guaaauu")
perro.hablar()
animal=Animales("miau")
animal.hablar()
pez=Pez("NADA")
pez.hablar()