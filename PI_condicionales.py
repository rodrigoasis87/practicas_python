# print("Programa de evaluación de notas de alumnos")
#
# nota_alumno = int(input("Introduce la nota del alumno: "))
#
# def evaluacion(nota):
#     valoracion = "Aprobado"
#     if nota < 5:
#         valoracion = "Suspenso"
#     return valoracion
#
# print(evaluacion(nota_alumno))
#
# print("Verificación de acceso")
#
# edad_usuario = int(input("Introduce tu edad por favor: "))
#
# if edad_usuario < 18:
#     print("No puedes pasar")
# else:
#     print("Puedes pasar")
# print("El programa ha finalizado")

# el elif permite entrar en el else cuando nada del programa se ha cumplido, y no solamente cuando no se cumple
# el if más cercano

#----------------------------------------------------------

# ejemplo de concatenación de operadores lógicos

# edad = -7
#
# if 0 < edad < 100:
#     print("Edad es correcta")
# else:
#     print("Edad es incorrecta")
#
# salario_presidente = int(input("Introduce el salario del presidente: "))
# print("Salario presidente: " + str(salario_presidente))
#
# salario_director = int(input("Introduce el salario del director: "))
# print("Salario director: " + str(salario_director))
#
# salario_jefe_area = int(input("Introduce el salario del jefe de área: "))
# print("Salario jefe de área: " + str(salario_jefe_area))
#
# salario_administrativo = int(input("Introduce el salario del administrativo: "))
# print("Salario administrativo: " + str(salario_administrativo))
#
# if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
#     print("Todo funciona correctamente")
# else:
#     print("Algo no anda como se esperaba")

print("Programa de becas Año 2022")

distancia_escuela = int(input("Introduce distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el número de hermanos: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No se te puede asignar una beca")

# con el ejemplo mostramos que cada una de las condiciones se tiene que dar sí o sí y en este caso
# podría resultar indeseado, por lo que si queremos darle más peso a una de las condiciones, en este caso
# la del salario familiar, deberíamos cambiar el "and" por el "or", que significa que si alguna de las condiciones
# anteriores no se cumple pero la del salario sí (es decir, tienen un salario menor), estaríamos priorizando
# el ingreso familiar

