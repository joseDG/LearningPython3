#manipulacion de diccionarios
from operator import le


dias_semana = {"Lunes":"Monday",
               "Martes":"Tuesday",
               "Miercoles":"Wendnesday",
               "Jueves":"Thursday",
               "Viernes":"Friday",
}

print(dias_semana["Lunes"])
print(dias_semana["Miercoles"])
print(dias_semana["Viernes"])

#Agregar elementos al diccionario
print(dias_semana)
dias_semana["Sabado"] = "Saturday"
dias_semana["Domingo"] = "Sunday"
print(dias_semana)

#Eliminar elementos del diccionario
del dias_semana["Lunes"]
print(dias_semana)

#Algunos metodos de los diciconarios
print("Numero de elementos del diccionario: ", len(dias_semana))
print("Elemento mayor del diccionario: ", max(dias_semana))
print("Elemento menor del diccionario: ", min(dias_semana))

#Metodos Propios
#copy => realzia una copia exacta 
#pop => obtiene el valor del elemento
#popitem => obtiene un elemnto aleatorio
#get=> obtiene el valor de la clave
#update => realzia una actualizacion de diccionarios
#setdefault => intenta insertar un elemento
#clear => elimina todos los elemntos del diccionario
#items => devuelve un objeto iterable
#keys => devuelve un objeto iterable
#values => devuelve un objeto iterable

print("Diccionario original: ", dias_semana)
dias_semana1 = dias_semana.copy()
print(dias_semana1)