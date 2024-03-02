'''Ejercicio 1

Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0

'''
def pedir():
    num1=int(input("Ingrese un numero:"))
    num2=int(input("Vuelva a ingresar un numero:"))
    if num1>num2:
        return 1
    elif num1<num2:
        return -1
    else:
        return 0

print(pedir())