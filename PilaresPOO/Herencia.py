class Animales():
    def habla(self):
        print("Yo soy un animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))
class Perro(Animales): #Estamos heredando todos los metodos y atributos de animales
    pass
class Gato(Animales):
    def __init__(self,animal):
        self.animal=animal
animal=Animales()
animal.habla()
perro=Perro()
perro.habla()
gato=Gato("Gato") #lo que esta entre comillas es el atributo que le paso a la clase que hereda el metodo de animales
gato.descripcion()