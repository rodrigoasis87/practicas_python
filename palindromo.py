def palindromo(palabra):
    texto = palabra.lower().replace(" ", "")
    reversa = texto[::-1]
    if texto == reversa:
        return True
    else:
        return False


def run():
    palabra = input("Escribe una palabra o una oración: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es palíndromo. ¡Intenta nuevamente!")


if __name__ == '__main__':
    run()