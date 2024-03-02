'''Ejercicio 2

Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.'''
def calculo():
    monto=float(input("Ingresa el valor del producto que estas pagando:"))
    iva=int(input(" Ingresa el valor del iva:"))
    if iva !=0:

        if iva>0:
            totalpagar=((monto*iva)/100) + monto
            return totalpagar
        
        else:
            print("El monto de iva no se puede calcular ya que es negativo")

    else:
        totalpagar=(monto*0.21)+monto
        return totalpagar
print("El total de su monto es:", calculo())