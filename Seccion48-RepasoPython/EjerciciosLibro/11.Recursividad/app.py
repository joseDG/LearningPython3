"""
NOTE

1. Un algoritmo recursivo debe tener un caso base.
2. Un algoritmo recursivo debe cambiar su estado y moverse hacia el caso base.
3. Un algoritmo recursivo debe llamarse a si mismo recursivamente.
"""
def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero-1)

factorial = int(input("Introduzca el numero del que quiere calcular el factorial :"))
print("El factorial de " + str(factorial) + " es: " + str(Factorial(factorial)))


def Potencia(base, expo):
    if expo <= 0:
        return 1
    else:
        return base * Potencia(base, expo-1)

base = int(input("Introduzca la base de la potencia: "))
expo = int(input("Introduzca el expoennete de la potencia: "))
print("El valor de " + str(base) + " elevado a " + str(expo) + " es: "
+ str(Potencia(base,expo)))