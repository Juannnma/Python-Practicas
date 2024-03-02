'''class FabricaTelefonos():
    marca="Nokia"

    def ElaborarHuawei(self): #el self nos permite englobaratributos a toda la clase
        self.marca="Huawei"

celular=FabricaTelefonos()
celular.ElaborarHuawei()
print(celular.marca)'''
'''class FabricaTelefonos():
    def __init__(self): #se ejecuta al iniciar el objeto 
        print("Estoy ejecutando el metodo init por que se creado un nuevo objeto")
celular=FabricaTelefonos()
'''
'''class FabricaTelefonos():
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color

celular=FabricaTelefonos("Nokia","Negro")
print(celular.marca)
print(celular.color)
'''


class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return ("El nombre de la persona es{} y tiene {} años".format(self.nombre,self.edad))
objeto=Persona("Juan",20)
print(objeto)
