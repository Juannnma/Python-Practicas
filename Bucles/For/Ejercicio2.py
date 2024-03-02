'''Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''
numero=int(input("Ingrese un numero:"))
segundo_numero=int(input("Ingrese un segundo numero:"))
for i in range(numero,segundo_numero + 1):
    if i % 2 == 0:
        continue
    print(i)
