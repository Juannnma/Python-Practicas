'''Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas'''
vocal=input("Ingrese una vocal, en minuscula por favor:")
consonante=input("Ahora una consonante en MAYUSCULA:")
remplazo1=consonante.lower()
reemplazo2=vocal.upper()
print("La vocal fue:{}\nLa vocal fue: {}".format(reemplazo2,remplazo1))