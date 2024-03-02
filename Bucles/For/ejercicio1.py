'''Ejercicio 1

Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''
for i in range(1,11):
    print (i)
numero=int(input("Ingrese un numero:"))
segundo_numero=int(input("Ingrese un segundo numero:"))
for i in range(numero,segundo_numero +1):
    print(i)