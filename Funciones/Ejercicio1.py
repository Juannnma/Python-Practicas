'''Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas'''
def add_list():
    lista = []
    cantidad = int(input("¿Cuántos números desea ingresar?: "))
    
    for i in range(cantidad):
        numeros = int(input("Ingrese un número: "))
        lista.append(numeros)
    
    print("Lista ingresada:", lista)
    return lista

def order_list(lista):
    lista.sort()
    lista_par = []
    lista_impar = []
    
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    
    print("Lista ordenada:", lista)
    print("Lista de números pares:", lista_par)
    print("Lista de números impares:", lista_impar)

mi_lista = add_list()
order_list(mi_lista)
