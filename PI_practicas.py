miLista = ["Juan", 13, 1, 1995]
miTupla = tuple(miLista)

nombre, dia, mes, agno = miTupla

print("Juan" in miTupla)
print(miTupla.count(13))
print(len(miTupla))

# list para convertir tupla en lista; tuple para convertir lista en tupla

# print "in" para saber si un elemento está en lista o tupla (devuelve True o False)

# count para saber cuántas veces se encuentra en una tupla o lista

# len para saber cuántos elementos tiene la lista (largo de la misma)

# (desempaquetado de tuplas) se pueden asignar variables a los elementos de una lista ordenándolos y
# guardándolos del otro lado del signo =

print(nombre)

# clase sobre diccionario, estructura de clave : valor

miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Italia":"Roma", "España":"Madrid"}

print(miDiccionario["Alemania"])

miDiccionario["Reino Unido"] = "Lisboa"

print(miDiccionario)

miDiccionario["Reino Unido"] = "Londres"

print(miDiccionario)

del miDiccionario["Reino Unido"]

print(miDiccionario)

# por supuesto que las claves pueden ser número y el valor un string o viceversa

miNuevaTupla = ["España", "Francia", "Italia", "Alemania"]

miNuevoDiccionario = {miNuevaTupla[0]:"Madrid", miNuevaTupla[1]:"París", miNuevaTupla[2]:"Roma", miNuevaTupla[3]:"Berlín"}

print(miNuevoDiccionario)