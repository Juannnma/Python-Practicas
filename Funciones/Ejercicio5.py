'''Ejercicio 1

Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

'''
def area_cuadrado(base,altura):
    area=base*altura
    return area
print("El area del cuadrado es:{}".format(area_cuadrado(10,5)))

def area_circulo(pi,radio):
    area=pi*radio**2
    return area
print("El area de un circulo es:{}".format(area_circulo(3.14159,5)))