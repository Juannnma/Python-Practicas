#sumar multiplos de 5 hasta llegar a 50---while
i= 0
suma= 0

numero_max=int(input("Introduce el numero maximo:"))
while i<numero_max:
    suma+= i
    i+=5
print("La suma es:",suma)