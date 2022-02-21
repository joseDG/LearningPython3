#LIBRERIA PARA NUMEROS ALEATORIOS
"""
randrange => numero aleatorio asignando un rango 
sample => devuelve una lista de numeros aleatorios
random => devuelve numero en coma flotante 
choice => selecciona un elemento de la lista 
"""
import random

print("Numero aleatorio del 1 al 1000: ", random.randrange(1000))
print("Lista aleatoria de numeros entre 1 y el 1000: ",random.sample(range(1000),3))
print("Numero aleatorio en coma flotante: ", random.random())
print("Eleccion aleatoria [python, java, c#, Ruby, go]:", random.choice(['python','go']))