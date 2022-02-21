from readline import insert_text


lista = ["Python", "RRa",2019,3,"Libro"]
print(lista)
print(lista[0])

#Concatenar listas
lista1 = ["camiseta","Pantalon"]
lista2 = ["zapatillas", "Camisa"]
print(lista1 + lista2)

print("tamano de la lista", len(lista2))

#Agregar elememtos a la lista
lista = ["manzana","pera"]
print(lista)
lista += lista + ["uvas"]
print(lista)

#permite reemplazar el valor
lista3 = ["carro","avion"]
print(lista3)
lista3[1] = "Barco"
print(lista3)

#permite multiplicar listas
lista4 = ["camiseta","pantalon"]
print(lista4)
lista_Resultante = lista4 * 3
print(lista_Resultante)

#permite ingresar dentro de otra lista
lista5 = ["camiseta",["calculadora", "esfero"],"zapatos"]
print(lista5)
print(lista5[0])
print(lista5[1])
print(lista5[1][0])
print(lista5[1][1])

#slice con listas
numeros = [1,2,3,4,5,6,7]
print(numeros)
lista_numeros = numeros[3:7]
print(lista_numeros)    
lista_numeros = numeros[6:]
print(lista_numeros)

#Metodos en las listas
append =>agrega elementos
insert => agrega elemento como parametro
remove => elimina la primera empezando de la izquierda 
reverse => inviert la lista
sort => ordena la lista  
pop => elimna la lista del elemento 
extend => anadade elementos de una lista. 
count => cuenta el numero de veces.
index => devuelve la posicion 
clear => elimna todos los eletnos de la lista 
