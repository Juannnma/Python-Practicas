'''Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]

'''
lista=[20, 50, "Curso", 'Python', 3.14]
print("ESTOS SON LOS VALORES ACTUALES DE LA LISTA: {}".format(lista))
dato1=(input("Ingrese un dato:"))
dato2=(input("Vuelva a ingresar un dato:"))
lista[0]=dato1
lista[1]=dato2
print(lista)