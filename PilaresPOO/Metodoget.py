class A():
    def __init__(self):
        self._cuenta=29
        self._contador=299
    @property #al agregar este decorador nos va indicar que el metodo get de abajo lo podemos llamar como un atributo
    def cuenta(self): #METODO GET
        return self._cuenta
    @property
    def contador(self):
        return self._contador
a=A()
print(a.cuenta) #metodo
print(a.contador)#metodo