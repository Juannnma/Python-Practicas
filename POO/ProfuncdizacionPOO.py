class FabricaTelefonos():
    def __init__(self,marca,*colores,**modelos):
        self.marca=marca
        self.colores=colores
        self.modelos=modelos

celular=FabricaTelefonos("Nokia","Negro","Rojo",m1=2020, m2=2023)

print(celular.marca)

print(celular.colores)
print(celular.modelos)
celular.memoria=128 #atributos temporales
print(celular.memoria)