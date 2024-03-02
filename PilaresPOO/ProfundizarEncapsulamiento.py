##aACCESO A LOS ATRIBUTOS
class A():
    def __init__(self):
        self._contador=0
        self._cuenta=0 #el _ le va indicara otro programador que no se modifique o se acceda por fuera a este atributo
    def incrementar(self):
        self._contador +=1
    def cuenta(self):
        return self._contador
    
a=A()

'''print(a.cuenta)
#Lo correcto seria usar el metodo get
a.cuenta=20
print(a.cuenta)'''
