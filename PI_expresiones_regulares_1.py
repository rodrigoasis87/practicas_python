import re

lista_nombres = ["Ana Gómez",
                 "María Martín",
                 "Sandra López",
                 "Santiago Martín",
                 "Sandra Fernández"]

for elemento in lista_nombres:
    if re.findall("^Sandra", elemento):
        print(elemento)

for elemento in lista_nombres:
    if re.findall("Martín$", elemento):
        print(elemento)


lista_urls = ["http://pildorasinformaticas.es",
              "ftp://pildorasinformaticas.es",
              "http://pildorasinformaticas.com",
              "ftp://pildorasinformaticas.com",
              "http://pildorasinformaticasespaña.com"]

for elemento in lista_urls:
    if re.findall("es$", elemento):
        print(elemento)

for elemento in lista_urls:
    if re.findall("[ñ]", elemento):
        print(elemento)

lista_especies = ["hombres",
                 "mujeres",
                 "mascotas",
                 "niños",
                 "niñas",
                 "camión",
                 "camion"]

for elemento in lista_especies:
    if re.findall("niñ[oa]s", elemento):
        print(elemento)

for elemento in lista_especies:
    if re.findall("cami[oó]n", elemento):
        print(elemento)