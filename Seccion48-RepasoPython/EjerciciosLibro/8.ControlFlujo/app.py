"""
NOTE 
Operadores Relacionales:
<  => menor
>  => mayor
<= => menor igual
>= => mayor igual
== = igual igual
!= = diferente
""" 

numero = int(input("Escriba un numero del al 1000: "))
if numero < 400:
    print("!El numero que has escritoes menor que 400!")
print("Has escrito el numero " + str(numero))

sumando1 = int(input("Escriba el primer sumando: "))
sumando2 = int(input("Escriba el segundo sumando: "))
resultado = sumando1 + sumando2
print("El resultado de la suma es: " + str(resultado))
if resultado%2==0:
    if resultado >= 1000:
        print("El resultado de la suma es par y mayor o igual que 1000")
    else:
        print("El resutlado de la suma es par")
else:
    if resultado >= 1000:
        print("El resultado de la suma impar")
    else: 
        print("El resulatado de la suma es impar")