class A():
    def __init__(self):
        self._cuenta=0
        self._contador=0
    @property #al agregar este decorador nos va indicar que el metodo get de abajo lo podemos llamar como un atributo
    def cuenta(self): #METODO GET
        return self._cuenta
    @cuenta.setter
    def cuenta(self, cuenta):
        self._cuenta=cuenta
    @property
    def contador(self):
        return self._contador
    @contador.setter
    def contador(self,contador):
        self._contador=contador

a=A()
print(a.cuenta) #metodo
a.cuenta=300
print(a.cuenta)
print(a.contador)#metodo
a.contador=23
print(a.contador)