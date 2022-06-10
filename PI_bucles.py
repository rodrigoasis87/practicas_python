import math

# contador = 0
#
# miEmail = input("Introduce tu dirección de email: ")
#
# for i in miEmail:
#     if (i == "@" or i == "."):
#         contador = contador + 1
#
# if contador == 2:
#     print("Email es correcto")
# else:
#     print("El email no es correcto")
#
# # destacar acá el uso del contador como estrategia, convención, dentro de los bucles
# # cuando nos interesa realizar acciones a partir del uso de los condicionales, es muy utilizada la estrategia
# # del contador en la que a cada acción que nos interese evaluar, un contador aumenta o disminuye su valor,
# # hasta encontrar el valor que necesitamos para ejecutar una acción
#
# # notación útil cuando queremos unir textos con variables sin tener que usar concatenaciones:
#
# for i in range(5):
#     print(f"valor de la variable {i}")
#
# for i in range(5, 10):
#     print(f"valor de la variable {i}")
#
# # ahora vemos cómo admite el range un tercer parámetro que indica de cuánto en cuánto corre
#
# for i in range(5, 50, 10):
#     print(f"valor de la variable {i}")
#
#
# # nuevo ejemplo con range, f y len
#
# valido = False
#
# email = input("Introduce tu email: ")
#
# # para la variable en el rango del largo de email
# for i in range(len(email)):
#
#     if email[i] == "@":
#
#         valido = True
#
# if valido == True:
#     print("Email correcto")
#
# else:
#     print("Email incorrecto")
#
# # bien, lo que "if email[i] == @" diciendo es básicamente "if [i] == @" porque i va recorriendo los caracteres
# # del mail ingresado hasta encontrar el arroba, mail solo le da el largo; por ahora es más complicado al pedo
# # que "for i in eMail" porque en vez de poner cualquier palabra para que la recorra la variable, se coloca un rango
# # que a su vez se conforma por un len que determina un número a partir del dato ingresado
#
# # ------------------------------------------------------------------------
#
# # bucle while
#
# i = 1
#
# while i<=10:
#     print("Ejecución " + str(i))
#     i = i + 1
#
# print("Terminó la ejecución")
#
# # ------------------------------
#
# edad = int(input("Por favor ingresa tu edad: "))
#
# while edad<0:
#     print("Has introducido una edad negativa, inténtalo nuevamente.")
#     edad = int(input("Por favor ingresa tu edad: "))
#
# print("Gracias.")

# ---------------------------------------------

print("Programa de cálculo de raíz cuadrada")

numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo.")

    if intentos == 2:
        print("No te quedan intentos. El programa ha finalizado.")

        break #para salir del bucle while

    numero = int(input("Introduce un número por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))



# ------------------------------------------------------

email = input("Ingresa tu email: ")

for i in email:
    if i=="@":
        arroba = True
        break

else:
    arroba = False

print(arroba)