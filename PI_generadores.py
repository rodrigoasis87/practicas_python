def generaPares(limite):
    num = 1
    miLista = []
    while num<limite:
        miLista.append(num*2)
        num = num + 1
    return miLista

print(generaPares(10))


# ------------------------------
# ahora con un generador, que devuelve un yield (construir un objeto iterable que va devolviendo uno en uno)

# explicado mejor, una función generador nos devuelve un OBJETO GENERADOR en el cual se van almacenando uno a uno,
# poco a poco, diversos elementos, esos elementos pueden ser de distinta índole (números, strings, listas, tuplas,
# diccionarios, etc)


def generaPares(limite):
    num = 1
    while num<limite:
        yield num*2
        num = num + 1

devuelvePares = generaPares(10)


# --------------------------------
# ahora con método next que nos devuelve los valores uno a uno


print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))

print("Aquí podría ir más código...")

print(next(devuelvePares))


# con un generador se generan valores infinitos siempre que las llamadas sean infinitas

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))


