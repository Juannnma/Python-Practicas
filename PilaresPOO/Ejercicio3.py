'''

Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

'''
class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas=llantas
        self.color=color
        self.precio=precio
    def mostrar_llantas(self):
        print("Mi tiene {}".format(self.llantas))

class Carro(Fabrica):
    def datos(self):
        print("La cantidad de llantas es de: {}".format(self.llantas))
        print("El color es de: {}".format(self.color))
        print("El precio es de: ${}".format(self.precio))
class Moto(Fabrica):
        def datos(self):
            print("La cantidad de llantas es de: {}".format(self.llantas))
            print("El color es de: {}".format(self.color))
            print("El precio es de: ${}".format(self.precio))
moto=Moto(2,"Negro",4000)
moto.datos()