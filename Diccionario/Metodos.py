diccionario={1:2,2:3,3:4}
diccionario2={4:5,6:7}
print(diccionario)

diccionario.pop(3)
print(diccionario)
print(diccionario.get(2)) #trae valores

diccionario.setdefault(4,5)
print(diccionario)
diccionario.update(diccionario2) #junta dos diccionarios
print(diccionario)
