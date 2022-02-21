lista = ["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o"]

for item in lista:
    print(item, end="")

print("\n")
#Ciclo While
i=0
while i<10:
    print(i, end="")
    i += 1 

print("\n")

pedirnumero = True
while pedirnumero:
    valor = int(input("Introducir un entero inferior a 10: "))
    if valor< 10:
        pedirnumero = False
    print("FIN: !Ha introducido un valor inferior a 10!")

print("\n")

for item1 in range(5):
    item2 =0
    while item2<3:
        print("Iteracion" + str(item1) +","+str(item2))
        item2 = item2 +1