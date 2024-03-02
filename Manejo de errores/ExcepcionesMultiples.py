'''while True:
    try:
        num1=int(input("Ingrese un numero:"))
        resultado=100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("NO SE PUEDE DIVIDIR ENTRE CERO")'''
'''
while True:
    try:
        EDAD=int(input("Ingrese tu edad:"))
        print("Tu edad es: ", EDAD)
        break
    except ValueError:
        print("HAS COLOCADO UN VALOR ERRONEO")'''
while True:
    try:
        EDAD=int(input("Ingrese tu edad:"))
        print("Tu edad es: ", EDAD)
        break
    except KeyboardInterrupt:
        print("HAS cancelado la ejecucion")