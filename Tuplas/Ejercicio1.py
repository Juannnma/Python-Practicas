'''Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

'''
meses_del_anio = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
año=int(input("Ingrese un año:"))
print("El mes correspondienbte es :", meses_del_anio[año-1])