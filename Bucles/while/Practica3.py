tabla=int(input("Introduce la tabla a multiplicar:"))
i=0

while i<=10:
    resultado= tabla*i
    print("{} x {}={}".format(tabla,i,resultado))
    i+=1