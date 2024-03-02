'''Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.'''
#extraño<-->tamaño
#desligo<-->amigo
    #riman<-->cuerpo
#sol<--->lol
#lo<-->yo
palabra1=str(input("Ingrese una palabra:"))
palabra2=str(input("Ingrese la segunda palabra palabra:"))

'''ult_tres_p1=palabra1[3:0]
ult_tres_p2=palabra2[3:0]
ult_dos_p1=palabra1[2:0]
ult_dos_p2=palabra1[2:0]
if ult_tres_p1==ult_tres_p2:
    print("Las palabras riman")
elif ult_dos_p1==ult_dos_p2:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")'''
#verificacion de la longitud de las palabras
if len(palabra1)<3 or len(palabra2) <3:
    print("No riman por que tienen menos de 3 caracteres")
#obtiene las tres ultimas de cada palabra y verifica si riman
elif palabra1[-3:] ==palabra2[-3:]: #ultimas 3 letras
    print("Las palabras riman")

#obtiene las dos ultimas de cada palabra y verifica si riman
elif palabra1[-2:]==palabra2[-2:]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")