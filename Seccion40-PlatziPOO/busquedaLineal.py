import random


def busquedaLineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
            break

    return match


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano es la lista? "))
    objetivo = int(input("Que numero quires encontrar? "))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busquedaLineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
