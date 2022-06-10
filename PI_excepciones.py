# def suma(nume1, nume2):
#     return nume1+nume2
#
# def resta(nume1, nume2):
#     return nume1-nume2
#
# def multiplicar(nume1,nume2):
#     return nume1*nume2
#
# def dividir(nume1,nume2):
#     try:
#         return nume1/nume2
#
#     except ZeroDivisionError:
#         print("no se puede dividir por cero")
#         return "operación no válida"
# while True:
#     try:
#         op1 = int(input("escriba el primero numero: "))
#         op2 = int(input("escriba el segundo numero: "))
#         break
#     except ValueError:
#         print("Los valores introducidos no son correctos. Inténtalo de nuevo.")
#
# operacion= input("¿que operacion quiere realizar de las siguientes (suma,resta,multiplicar,dividir)? : ")
#
# if operacion == "suma":
#    print(suma(op1,op2))
# if operacion == "resta":
#     print(resta(op1,op2))
# if operacion =="multiplicar":
#     print(multiplicar(op1,op2))
# if operacion == "dividir":
#     print(dividir(op1,op2))

# ---------------------------------------------------------

# otro ejemplo

# def divide():
#
#     try:
#
#         op1 = float(input("Introduce el primer número: "))
#
#         op2 = float(input("Introduce el segundo número: "))
#
#         print("La división es: " + str(op1/op2))
#
#     except ValueError:
#
#         print("El valor introducido es erróneo.")
#
#     except ZeroDivisionError:
#
#         print("No se puede dividir por cero")
#
#     print("Cálculo finalizado")
#
# divide()

# # también se puede colocar finally: para ejecutar sí o sí la línea final, por ejemplo en conexiones con bases de datos
#
# # ahora vemos la excepción raise, una excepción personalizada, que veremos en POO, ya que el error personalizado
# # raise es una clase class

# def evaluaEdad():
#
#     if edad<0:
#         raise TypeError("No se permiten edades negativas")
#     if edad<20:
#         return "Eres muy joven"
#     elif edad<40:
#         return "Eres joven"
#     elif edad<65:
#         return "Eres maduro"
#     elif edad<100:
#         return "Cuídate"
#
# print (evaluaEdad(18))

import math

def calculaRaiz(num1):

    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = int(input("Introduce un número: "))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")