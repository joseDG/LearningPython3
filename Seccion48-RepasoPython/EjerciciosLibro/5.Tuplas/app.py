tupla = ('casa',2,345,'Perro',99,99)
print("Elementos de la tupla: ", tupla)
print("Elementos de la posicion 0: ", tupla[0])
print("Elementos de la posicion 1: ", tupla[1])
print("Elementos de la posicion 2: ", tupla[2])

#agregando metodo count
print("Numero de elemntos en la tupla: ", tupla.count(99))
#se puede verificar la posicion del elemento
print("Posicion que ocupa el elemento Perro:", tupla.index("Perro"))

tupla2 = (1,2,3,4,5,6,7,8,9)
print(tupla2)
print(tupla2[4:9])
print(tupla2[:3])

#Uniones de tuplas
tupla3 = (29,"tv")
tupla4 = (1,2,3)
print("Tamano de la tupla:", len(tupla3))
print(tupla3  + tupla4)

#Multiplciacion de tuplas
tupla5 = (2,3,4,5,6)
print(tupla5)
tuplaresultante = tupla5 * 4
print(tuplaresultante)
