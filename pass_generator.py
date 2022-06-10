import random


def create_password():
    may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'X', 'Y', 'Z']
    min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    cha = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~',
           '°', '^', '&', '$', '#', '"']

    # creo una lista única con todas las demás
    character = may + min + num + cha

    # ahora creo una lista vacía donde vamos a poner caracteres aleatorios para generar la contraseña
    # acá guardamos caracteres elegidos al azar de la lista anterior
    random_pass = []

    for i in range(15):
        random_character = random.choice(character)
        random_pass.append(random_character)

    random_pass = "".join(random_pass)
    return random_pass


def run():
    password = create_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == "__main__":
    run()