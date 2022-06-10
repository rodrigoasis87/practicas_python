# class Coche():
#     largoChasis = 250
#     anchoChasis = 120
#     ruedas = 4
#     enMarcha = False
#
#     def arrancar(self):
#         self.enMarcha = True
#
#     def estado(self):
#         if self.enMarcha == True:
#             return "El coche está en marcha."
#         else:
#             return "El coche está parado."
#
# miCoche = Coche()
#
# print("El largo del coche es: ", miCoche.largoChasis)
# print("El coche tiene ", miCoche.ruedas, " ruedas.")
# miCoche.arrancar()
#
# print(miCoche.estado())

# # ahora nos va a arrojar que está en marcha porque hemos arrancado el coche cuando llamamos el método
# # miCoche.arrancar() (en los métodos/estados poner siempre los paréntesis())

# # la palabra reservada self es reemplazada por el nombre del objeto, permitiendo así que el objeto acceda
# # a cada uno de los atributos, comportamientos o estados, por ejemplo "miCoche.arrancar"

# print("--------------A continuación creamos el segundo objeto------------------")
#
# miCoche2 = Coche()
# print("El largo del coche es: ", miCoche2.largoChasis)
# print("El coche tiene ", miCoche2.ruedas, " ruedas.")
#
# print(miCoche2.estado())

# -------------------------------------------------------------------------------

# # ahora realizamos algunas modificaciones en el código, para que el método arrancar
# # no solo se encargue de arrancar el coche sino también de informarnos el estado, pasando
# # el código que tenemos en el método "estado" al método "arrancar", agregando un parámetro
# # en el método, al que llamaremos "arrancamos", para que almacene el parámetro que ingresemos
# # cuando llamemos al método y lo asigne a la variable "enMarcha"


class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # ENCAPSULAMIENTO dos guiones bajos para que resulte inaccesible por fuera de la clase
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha == True:
            chequeo = self.__chequeo_interno()

        if self.__enMarcha == True and chequeo == True:
            return "El coche está en marcha."

        elif self.__enMarcha == True and chequeo == False:
            return "Algo ha ido mal en el chequeo, no podemos arrancar"

        else:
            return "El coche está parado."

    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis,
              " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno.")

        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False

# "zona de llamadas"

miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("--------------A continuación creamos el segundo objeto------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

# miCoche2.ruedas = 2 ----  igual no funcionaría porque está encapsulado

miCoche2.estado()
