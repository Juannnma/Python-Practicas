'''Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal

'''
letra=str(input("Ingrese una letra:"))

if letra.lower()=="a" or letra== "e" or letra=="i" or letra=="u":
    print("Es vocal")
else:
    print("No es vocal")
