def funcion_decoradora(funcion_parametro):
    def funcion_interior():

        # acciones adicionales que decoran
        print("Vamos a realizar un cálculo: ")

        # llamado de la función que ingresa al parámetro con el nombre de funcion_parametro
        funcion_parametro()

        # más acciones adicionales que decoran
        print("Hemos terminado el cálculo")

    return funcion_interior

@funcion_decoradora
def suma():
    print(15 + 20)

@funcion_decoradora
def resta():
    print(30 - 10)

suma()

resta()

