'''''Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''
numero=int(input("Ingrese un numero para saber su tabla:"))
i=0
mult=0
while i <= 10:
    mult=numero*i 
    print("{} x {}={}".format(numero,i,mult))
    i+=1 #rompe el bucle
