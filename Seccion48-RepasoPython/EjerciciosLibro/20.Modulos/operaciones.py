def sumar(sum1, sum2):
    return sum1 + sum2

def Restar(minuendo, sustraendo):
    return minuendo-sustraendo

def Multiplicar(multiplicando, multiplicador):
    return multiplicando*multiplicador

def Dividir(dividendo, divisor):
    try:
        resultado = dividendo/divisor
        return resultado
    except ZeroDivisionError:
        return -1

def Factorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * Factorial(numero-1)

def Potencia(base, exponente):
    if exponente <= 0:
        return 1
    else:
        return base * Potencia(base,exponente-1)