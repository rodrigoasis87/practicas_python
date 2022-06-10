from io import open

# crear variable archivo_texto con la orden de apertura de un archivo, cuyos parámetros son el nombre y el tipo de uso

# archivo_texto = open("archivo.txt", "w")

# como estamos en modo escritura, podemos guardar una frase en una variable y luego usar el método
# write para pasar como argumento la variable con la frase (podría escribirse la frase directamente dentro
# de los paréntesis del parámetro del método)

# archivo_texto.write(frase)

# luego cerramos el archivo

# archivo_texto.close()

# corremos el programa

# -----------------------------------------------------------------
# ahora abrimos el archivo para modo lectura

# archivo_texto = open("archivo.txt", "r")

# guardamos en una variable lo que podamos leer del archivo con el método read()
# texto = archivo_texto.read()

# cerramos el archivo (lo cerramos de la memoria)
# archivo_texto.close()

# imprimimos la variable
# print(texto)

# corremos el programa

# también podríamos usar el método readlines() para leer las líneas como listas, lo que nos permitiría
# manipularlas

# linas_texto = archivo_texto.readlines()
#
# archivo_texto.close()
#
# print(linas_texto[0])

# corremos el programa

# -------------------------------------------
# ahora usamos el método append para añadir líneas de texto

# archivo_texto = open("archivo.txt", "a")
#
# archivo_texto.write("\nEn realidad siempre es una buena ocasión para estudiar Python")
#
# archivo_texto.close()

# cada vez que corro el programa se imprime una línea más

# ----------------------------------------------------------------

archivo_texto = open("archivo.txt", "r+")

# print(archivo_texto.read())

# con esto elegimos la posición del puntero para que vuelva al inicio y nos lea la información dos veces
# archivo_texto.seek(0)

# print(archivo_texto.read())

# la diferencia entre seek y read es que seak marca dónde empieza y read lee hasta; si por ejemplo
# queremos diseñar una línea de código para que empiece a leer desde la mitad, podríamos decir:

# archivo_texto.seek(len(archivo_texto.read())/2)

# print(archivo_texto.read())

# print(archivo_texto.readlines())

lista_texto = archivo_texto.readlines()

lista_texto[2] = "Esta línea ha sido incluida desde el exterior\n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()