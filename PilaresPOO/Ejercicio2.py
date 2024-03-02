'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

'''
class Calculadora():
    def __init__(self):
        self.valor1 = int(input("Ingrese un valor: "))
        self.valor2 = int(input("Vuelva a ingresar un valor: "))

    def suma(self):
        self.suma_resultado = self.valor1 + self.valor2
        return "La suma de {} + {} = \nDa como resultado: {}".format(self.valor1, self.valor2, self.suma_resultado)

    def resta(self):
        self.resta_resultado = self.valor1 - self.valor2
        return "La resta de {} - {} = \n Da como resultado: {}".format(self.valor1, self.valor2, self.resta_resultado)

    def multiplicacion(self):
        self.multiplicacion_resultado = self.valor1 * self.valor2
        return "La multiplicacion de {} * {} = \n Da como resultado: {}".format(self.valor1, self.valor2, self.multiplicacion_resultado)

    def division(self):
        self.division_resultado = self.valor1 / self.valor2
        return "La division de {} / {} =\n Da como resultado: {}".format(self.valor1, self.valor2, self.division_resultado)

while True:
    print("BIENVENIDO A CALCULADORA ONLINE")
    print("¿Qué desea hacer?")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        calcular = Calculadora()
        print(calcular.suma())
    elif opcion == "2":
        calcular = Calculadora()
        print(calcular.resta())
    elif opcion == "3":
        calcular = Calculadora()
        print(calcular.multiplicacion())
    elif opcion == "4":
        calcular = Calculadora()
        print(calcular.division())
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")
