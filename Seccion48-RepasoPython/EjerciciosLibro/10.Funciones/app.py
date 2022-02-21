def Hola():
    print("Hola te giusta python")
print("Primera invocacion: ", end="")
Hola()
print("Segunda invocacion: ", end="")
Hola()

def Hola():
    return "Hola Te gusta Python?"
print("Primera invocacion: " + Hola())


def EsParOImpar(param):
    if param%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

numero = int(input("Introduce un numero:"))
EsParOImpar(numero)


def Multiplicar(param1, param2):
    return param1 * param2

multiplicar = int(input("Introduce el multiplicador: "))
multiplicador = int(input("Introduce el multiplicador: "))
resultado = Multiplicar(multiplicar, multiplicador)
print("El resultaod es: ", resultado)

def Sumar(*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado

resultado = Sumar(3,87,45,3,33,25,345,99)
print("El resultado de la suma" , resultado)


def Variables():
    variable = 3
    print("Valor dentro de la funcion: " + str(variable))

variable = 5
Variables()
print("Variable en el programa principal: " + str(variable))


def Variables():
    global variable 
    print("Valor dentro de la funcion: " + str(variable))
    variable = 3
    print("Valor dentro de la funcion: " + str(variable))

variable = 5
print("Variables en el programa principal: "  + str(variable))
Variables()
print("Variables en el programa principal: "  + str(variable))
