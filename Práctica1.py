menu = """Bienvenido/a al conversor de monedas.

1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Para conocer su valor monetario en dólares, por favor seleccione la opción correcta: """

opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos Argentinos tienes?: "))
    valor_dolar = 215
    dolares = str(round(pesos / valor_dolar, 2))
    print("Tienes $" + dolares + " dólares")
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos Colombianos tienes?: "))
    valor_dolar = 65
    dolares = str(round(pesos / valor_dolar, 2))
    print("Tienes $" + dolares + " dólares")
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos Mexicanos tienes?: "))
    valor_dolar = 25
    dolares = str(round(pesos / valor_dolar, 2))
    print("Tienes $" + dolares + " dólares")
else:
    print("Por favor ingresa una opción válida")

""" guardamos en una variable un input para que recepte los datos ingresados por el usuario,
luego le damos a esa misma variable la definición de tipo de dato con la función float() para que el dato ingresado ahí
desde el input se transforme a número decimal

luego en otra variable fijamos un número para usar en el cálculo (ese número será una constante)

luego en otra variable guardamos el cálculo que va a surgir de dividir el valor ingresado (que ingresará como string 
pero se transforma a float, por el valor ya numérico fijado en la constante valor_dolar

finalizando, al resultado obtenido y guardado en la variable, lo volvemos a transformar en un string con la 
función str()

de esta manera, y por último, devolveremos mediante la función print() 
en la aplicación un tipo de dato igual al que ingresó el usuario pero transformado en el proceso"""

pesos = input("¿Cuántos pesos tienes?: ")
pesos = float(pesos)

valor_dolar = 215

dolares = round(pesos / valor_dolar, 2)
"""que es la versión simplificada de hacer
dolares = pesos / valor_dolar
dolares = round(dolares, 2)"""

dolares = str(dolares)

print("Tienes $" + dolares + " dólares")

""" espacio antes de crear el código a la inversa """

dolares = float(input("¿Cuántos dólares tienes?: "))

valor_peso = 0.00465

pesos = str(round(dolares / valor_peso, 2))

print("Tienes $" + pesos + " pesos")

""" espacio antes de crear el código a la inversa """

