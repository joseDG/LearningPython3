#Funciones mas de un parametro
def volume(a, b, c):
    return a * b * c

#funciones pueden tener un parametro por defecto
def converter(feet, coefficient = 3.2808):
    meters = feet / coefficient
    return meters
 
print(converter(10))

#funciones con keyword
def volume(a, b, c):
    return a * b * c
 
print(volume(1, b=2, c=10))

#funciones con *args
def find_max(*args):
    return max(args)
print(find_max(3, 99, 1001, 2, 8))

#funciones con kwargs
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))

#funciones con elementos
def cubo_volumen(a, b, c=10):
    return a * b * c 
print(cubo_volumen(2, b=3))