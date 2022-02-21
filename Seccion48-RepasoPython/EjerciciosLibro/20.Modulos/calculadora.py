from math import factorial
import operaciones

def Sumar():
    sum1 = int(input("Sumando uno:"))
    sum2 = int(input("Sumando dos:"))
    print("La suma es:",operaciones.sumar(sum1, sum2))

def Restar():
    minuendo = int(input("Minuendo:"))
    sustranendo = int(input("Sustraendo:"))
    print("La resta es:",operaciones.Restar(minuendo,sustranendo))

def Multiplicar():
    multiplicando = int(input("Multiplicando:"))
    multiplicador = int(input("Multiplicador:"))
    print("La Multiplicacion es:",operaciones.Multiplicar(multiplicando,multiplicador))

def Dividir():
    dividendo = int(input("Dividendo:"))
    divisor = int(input("Divisor:"))
    print("La division es:",operaciones.Dividir(dividendo, divisor))

def Factorial():
    factorial = int(input("Introduzca el numero del que quiere calcular el factorial"))
    print("El factorial de " + str(factorial) + "es:"+ str(operaciones.Factorial(factorial)))



def Calculadora():
    fin = False
    while not(fin):
        opc = int(input("Opcion:"))
        if(opc==1):
            Sumar()
        elif(opc==2):
            Restar()
        elif(opc==3):
            Multiplicar()
        elif(opc==4):
            Dividir()
        elif(opc==5):
            Factorial()
        elif(opc==6):
            fin = 1

print("""**********
Calculadora
**************
Menu
1) Suma
2) Resta
3) Multiplicar
4) Division
5) Factorial
6) Salir""")
Calculadora()