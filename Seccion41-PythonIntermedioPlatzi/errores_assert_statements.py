# son exccepciones moderna en la que una muestra el lado positivo o negativo
# son mensajes TRUE O FALSE
# es una alternativa para crear este tipo de excepciones
def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacia"
    return string == string[::-1]


print(palindrome(""))


def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = int(input("Ingrese un numero: "))
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Termino mi programa")


if __name__ == "__main__":
    run()
