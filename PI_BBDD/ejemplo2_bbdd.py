import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# vemos las 3 primeras líneas en las que importamos sqlite, creamos/nos conectamos a la base de datos y
# creamos el cursor guardándolo en una variable. Estos 3 primeros pasos son fijos en cada acción que realizamos.

# miCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#     PRECIO INTEGER,
#     SECCION VARCHAR(20)
#     )
# ''')
#
# productos = [
#
#     ("PELOTA", 20, "JUGUETERÍA"),
#     ("PANTALÓN", 15, "CONFECCIÓN"),
#     ("DESTORNILLADOR", 25, "FERRETERÍA"),
#     ("JARRÓN", 45, "CERÁMICA")
#
# ]
#
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL, ?, ?, ?)", productos)

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'CONFECCIÓN'")

# los siguientes comandos son para imprimir en consola la consulta que hicimos anteriormente
# productos = miCursor.fetchall()
#
# print(productos)


# miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'PELOTA'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4")

# el commit es para hacer efectiva la acción
miConexion.commit()

# close para cerrar luego de cada acción
miConexion.close()