'''Ejercicio 1

Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''
class Estudiante():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def __str__(self):
        if self.nota>=6:
            return "Estimado {},su nota es: {} por lo tanto esta aprobado".format(self.nombre,self.nota)       
        else:
            return "Estimado {},su nota es: {} por lo tanto esta desaprobado".format(self.nombre,self.nota)
    
print("BIENVENIDO AL SISTEMA DE NOTAS")
        
nombre_alumno=str(input("Ingrese su nombre para obtener su situacion academica:"))
nota_alumno=float(input("Ingrese su calificacion por favor:"))
estudiante=Estudiante(nombre_alumno,nota_alumno)
print(estudiante)


