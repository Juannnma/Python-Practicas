def factorial():
    # from math import factorial
    numero=int(input("Ingresa tu numero entero y positivo:"))
    if numero >0:
          # print(factorial(numero))
        factorial=1
        for i in range(1,numero+1):
            factorial*=i
        print(factorial)
    else:
        print("El numero es negativo y no podemos proceder")
factorial()