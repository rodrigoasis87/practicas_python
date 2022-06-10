class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utlizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando ocho ruedas")


def desplazamientoVehiculo(vehiculo):

    vehiculo.desplazamiento()

miVehiculo = Camion()

desplazamientoVehiculo(miVehiculo)

miVehiculo2 = Coche()

desplazamientoVehiculo(miVehiculo2)