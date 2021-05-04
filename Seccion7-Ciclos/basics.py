monday_temperatures = [9.1, 8.5, 7.6 ]

for temperaturas in monday_temperatures:
    print(round(temperaturas))
    print("Done")

for letter in "Hello":
    print(letter.title())

#ejercicio 1
colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)

#ejercicio 2
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

#ejercicio 3
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

#Recorrido con los diccionarios
estudiantes = {"Maria": 9.1, "Andres": 7.1, "Raul": 8.1, "Jose": 6.1}

for grades in estudiantes.values():
    print(grades)

#Ejemplo diccionarios
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

#Ejemplo
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

#Ejemplo con diccionarios
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))

#ejemplo 2 diccionarios
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))