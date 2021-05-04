temps = [221, 234, 340, 230]

nuevos_tiempos = [temp / 10 for temp in temps]

nuevos_tiempos = [temp / 10 if temp != -9999 else 0 for temp in temps]

print (nuevos_tiempos)

#ejercicio
def foorr(lst):
    return [i for i in lst if  isinstance(i, int)]

#ejercicio2
def foo(lst):
    return [i for i in lst if i > 0 ]

#ejercio 3
def foor(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

#ejerco
def fooe(lst):
    return sum([float(i) for i in lst])

#lsita
[i*2 for i in [1, 5, 10]]

#lsita con condicion if
[i*2 for i in [1, -2, 10] if i>0]

#lsita con compresion if-else
[i*2 if i>0 else 0 for i in [1, -2, 10]]