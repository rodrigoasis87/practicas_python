import sqlite3

miConexion = sqlite3.connect("PrimeraBase")

miCursor = miConexion.cursor()

# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

# variosProductos = [
#
#     ("CAMISETA", 10, "DEPORTES"),
#     ("JARRÓN", 50, "CERÁMICA"),
#     ("CAMIÓN", 30, "JUGUETERÍA")
#
# ]
#
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for p in variosProductos:
    print("Nombre artículo:", p[0], " Sección:", p[2])

miConexion.commit()

miConexion.close()