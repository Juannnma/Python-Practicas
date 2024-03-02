class FabricaTelefonos():
    marca="Samsung"
    Color= "Negro"
    Año=2020
    Almacenamiento=128 
    def llamar(self,mensaje): #metodo de instancia que es el que yo creo desde 0
        return mensaje
    def agendar(self):
        print("Agende el 8 de enero")

celular=FabricaTelefonos()
print("LAS CARACTERISTICAS DE TU TELEFONO SON: ")
print(celular.marca)
print(celular.Color)
print(celular.Año)
print(celular.Almacenamiento)
print(celular.llamar("Hola con quien hablo?"))
(celular.agendar())