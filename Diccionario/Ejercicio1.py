'''Ejercicio 1

En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.

{"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"'''
capitales={"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}
pais=str(input("Ingrese un pais por favor:"))

'''capital =capitales.get(pais)

if capital:
    print(f"La capital de {pais} es {capital}")
else:
    print(f"Lo siento no podemos encontrar informacion de {pais}")'''
letra=pais.capitalize() in capitales
if letra== True:
    print(capitales[pais.capitalize()])
else:
    print("Su pais no se encuentra en la web")