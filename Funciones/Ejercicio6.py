'''Ejercicio 2

Escribir una función que reciba una muestra de números en una lista y devuelva su medida.'''
def muestra(*tupla):
    print(len(tupla))
    for i in tupla:
        print(i)

muestra(2,3,5)   