import pickle

class Persona:

# empezamos a aplicar lo aprendido en clases anteriores y quiero terminar de entender la lógica del armado de las
# clases, viendo que cada uno de los bloques de acciones se nombran con el método def, ya que cada bloque cumple
# una función, por eso es un método, y por eso inicia con la palabra reservada def; la primera es un método especial
# def init ya que su función es la de inicializar la clase, y se comienza por la definición de atributos;
# después creamos un método según cada cosa que querramos que haga la clase; si queremos que imprima algo,
# que devuelva algo, que forme una frase devolviendo una serie de objetos, armamos un método con un def y
# con una acción reservada (o no, también podemos crear la función nosotrxs).
# También podemos inicializar la clase con el init o simplemente podemos guardar algunas variables dentro
# de la clase sin inicializar, como un contador o una lista vacía.

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

# clase para guardar datos en listas que vayan a ficheros externos y ahí se almacenen para ser leídas
# método para agregar personas a las listas y método para leer las personas almacenadas en listas

    personas = []

    # creamos un constructor para que al instanciar la clase se llame inmediatamente al constructor y se
    # inicialice la clase
    def __init__(self):

        listaDePersonas = open("ficheroExterno", "ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero está vacío")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente:")
        for p in self.personas:
            print(p)

# es necesario primero crear el objeto a instancia de la clase ListaPersonas para luego llamar a los métodos
miLista = ListaPersonas()

# persona = Persona("Sandra", "Femenino", 29)
# persona = Persona("Antonio", "Masculino", 39)

# acá llamamos el método del objeto y le pasamos el parámetro para que el método se ejecute guardando la información
miLista.agregarPersonas(persona)


miLista.mostrarInfoFicheroExterno()

# p = Persona("Rodrigo", "Masculino", 34)
# miLista.agregarPersonas(p)
#
# p = Persona("Joa", "Femenino", 28)
# miLista.agregarPersonas(p)

# acá llamamos el método del objeto y le pasamos el parámetro para que el método se ejecute mostrando la información
miLista.mostrarPersonas()