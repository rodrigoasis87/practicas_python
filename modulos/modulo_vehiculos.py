class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena)

class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado = cargar

        if self.cargado == True:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta está vacía"

class Moto(Vehiculo): # construimos subclase a partir de la clase Vehiculo
    hcaballito = "" # acá vemos que no utiliza el self antes de la variable

    def caballito(self):
        self.hcaballito = "Haciendo caballito"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha, "\nAcelerando: ",
              self.acelera, "\nFrenando: ", self.frena, "\nCaballito: ", self.hcaballito)

class VElectricos(): # no es necesario citar a Vehiculo en este caso ya que es una clase autónoma y estamos
    # probando la herencia múltiple; en este caso es necesario agregar los parámetros marca y modelo
    # con la funcion super() ya que que a la hora de construir la clase Bicicleta, le pasamos primero como
    # parámetro VElectricos antes que Vehiculo, y con ello se cruzan los métodos constructores __init__,
    # por lo que super() nos permite definir también los parámetros marca y modelo

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda", "CBR") # construimos instancia/objeto (miMoto) de la clase Moto, pasando como parámetros
# marca y modelo, que no estaban definidos en el constructor

miMoto.caballito() # llamada al estado caballito para que se active

miMoto.estado() # llamada al estado de miMoto, que va a imprimir de la clase Moto y no de la clase Vehiculo, ya que
# es de la clase Moto desde donde se instancia el objeto

miFurgoneta = Furgoneta("Renault", "Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True)) # la llamada es diferente de la de miMoto, ya que el método en moto devuelve un print
# mientras que furgoneta devuelve un return, por lo que hay que printear en el llamado

# creamos clase con herencia múltiple
class BicicletaElectrica(VElectricos, Vehiculo):
    pass

miBiciElectrica = BicicletaElectrica("Orbea", "BMX")

miBiciElectrica.estado()
