def media(lista):
    print("Inicio Funcion")
    la_media = sum(lista) / len(lista)
    return la_media

mi_media = media([0,3,4])
print(mi_media)

#Creacion de IF
def mediak(valor):
    if type(valor) == dict:
        la_media = sum(valor.values()) / len(valor)
    else:
        la_media = sum(valor) / len(valor)

    return la_media

lunes_temperatura = [8.8, 9.1, 6.3]
estudiantes = {"Jose":9.4, "Maria":9.4, "Mnesa": 9.4}

print(mediak(estudiantes))

#Ejercico de tempearatura
def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"