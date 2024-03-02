class Persona():
    def __init__(self,nombre,edad,dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    def __str__(self):
        return "El nombre de la persona es {} con {} años, con el dni {}".format(self.nombre,self.edad,self.dni)
persona1=Persona("Juan",20,44539139)
print(persona1)