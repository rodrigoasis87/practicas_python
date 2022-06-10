import re

nombre1 = "Sandra López"

nombre2 = "Antonio Gómez"

nombre3 = "María López"

if re.match("Sandra", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")


