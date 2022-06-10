# class Matematica:
#     def sumar(self):
#         self.n1 = 2
#         self.n2 = 3
#
# s = Matematica()
#
# s.sumar()
#
# print(s.n1 + s.n2)
#
# #hasta acá la forma ineficiente de aplicar un método
#
# class Ropa:
#     def __init__(self):
#         self.marca = "Willow"
#         self.talle = "M"
#         self.color = "Rojo"
#
# camisa = Ropa()
#
# print(camisa.talle)
#
# class Calculadora:
#     def __init__(self, n1, n2):
#         self.suma = n1 + n2
#         self.resta = n1 - n2
#         self.producto = n1 * n2
#         self.division = n1 / n2
#
# operacion = Calculadora(2, 5)
#
# print(operacion.producto)

#-------------------------------------------------------------------

# viejo Format

class Persona:
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    def descripcion(self):
        return "{} tiene {}".format(self.nombre, self.año)

    def comentario(self, frase):
        return "{} dice: {}".format(self.nombre, frase)

doctor = Persona("Rodrigo", 34)
print(doctor.descripcion())
print(doctor.comentario("las almas repudian todo encierro"))

# nuevo Format

class Persona:
    pass
    # recomiendan poner el pass porque los atributos no están en la clase sino en el constructor
    # el __init__ es un constructor que alberga los atributos
    def __init__(self, nombre, año):
        self.nombre = nombre
        self.año = año

    # acá colocamos los métodos
    def descripcion(self):
        return f"{self.nombre} tiene {self.año}"

    def comentario(self, frase, otrafrase):
        return f"{self.nombre} dice: {frase}, pero en realidad {otrafrase}"

doctor = Persona("Rodrigo", 34)
print(doctor.descripcion())
print(doctor.comentario("las almas repudian todo encierro", "lo dijo Luis"))