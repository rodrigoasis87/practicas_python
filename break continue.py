def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)
    #
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break

    frase = input("Ingresa una frase: ")
    for letra in frase:
        if letra == "o":
            break
        print(letra)
        # a diferencia del bloque de código anterior, en el que print está encima de la condición break
        # acá corta antes de imprimir la "o"; en el anterior sí imprime el 5678



if __name__ == "__main__":
    run()