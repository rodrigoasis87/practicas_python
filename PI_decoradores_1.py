def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):

        # acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        # llamado de la función que ingresa al parámetro con el nombre de funcion_parametro
        funcion_parametro(*args, **kwargs)

        # más acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7, 5, 8)

resta(8, 3)

potencia(base = 5, exponente = 3)