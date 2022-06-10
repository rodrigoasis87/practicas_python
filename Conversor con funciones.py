def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos + " tienes?: "))
    dolares = str(round(pesos / valor_dolar, 2))
    print("Usted tiene $" + dolares + " dólares")

dolar_arg = 215
dolar_col = 65
dolar_mex = 25

inicio = """Bienvenido/a al conversor de monedas. A continuación le dejamos las siguientes opciones de conversión:

1 - Pesos Argentinos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Por favor, seleccione la moneda que desea convertir a dólares: """

opcion = int(input(inicio))

if opcion == 1:
    conversor("argentinos", dolar_arg)
elif opcion == 2:
    conversor("colombianos", dolar_col)
elif opcion == 3:
    conversor("mexicanos", dolar_mex)
else:
    print("Por favor ingresa una opción válida")