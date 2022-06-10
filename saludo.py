import datetime

class Saludo():

    # método mágico para inicializar un objeto
    def __init__(self, nombre):
        self.nombre = nombre
        self.hora = datetime.datetime.now().hour
        self.minutos = datetime.datetime.now().minute

    # método mágico para mostrar los datos de un objeto en string
    def __str__(self):
