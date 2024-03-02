class A():
    def primero(self):
        return("Esta es la clase a")
class B():
    def segunda(self):
        return("Esta es la clase b")
class C(A,B):
    pass

c=C()
print(c.primero())
print(c.segunda())