'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

p1=float(input("Ingrese su primer nota:"))
p2=float(input("Ingrese su segunda nota:"))
p3=float(input("Ingrese su tercer nota:"))
EP=float(input("Ingrese su nota del parcial:"))
EF=float(input("Ingrese su nota de examen final:"))
PP=(p1+p2+p3)/3
PROM=(PP+2*EP*3*EF)/6
print("Su promedio final es \nPROMEDIO:",PROM)