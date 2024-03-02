nombre=str(input("Ingresa tu nombre:"))

if nombre=="Juan":
    edad=int(input("Ingresa tu edad:"))
    if edad>=18:
        print(nombre,"Es mayor!")
    else:
        print(nombre,"Es menor")
else:
    print("Tu nombre no es el que interesa")