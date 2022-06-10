import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    vidas = 5
    while numero_aleatorio != numero_elegido:
        if numero_aleatorio > numero_elegido:
            vidas -= 1
            print("Te quedan " + str(vidas) + " vidas ¡Deberás buscar un número más grande!")
        if numero_aleatorio < numero_elegido:
            vidas -= 1
            print("Te quedan " + str(vidas) + " vidas ¡Deberás buscar un número más chico!")
        if vidas == 0:
            print("Ya no te quedan vidas ¡Mejor suerte la próxima vez!")
            break
        else:
            print("¡Has acertado!")

        numero_elegido = int(input("Elige otro número: "))




if __name__ == "__main__":
    run()