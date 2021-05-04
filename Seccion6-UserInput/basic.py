user_input = input("Ingresa tu nombre: ")
mensaje = "Hola %s" % user_input
mensaje = f"Hola {user_input}"
print(mensaje)

name = input("Ingrese tu nombre: ")
apellido = input("Ingrese su apellido: ")
cuando = "dia"

mensaje = "Hola %s %s" % (name, apellido)
mensaje = f"Hola {name} {apellido}. Donde estas {cuando} "
print(mensaje)

#ejercicio
def foo(name):
    return "Hi %s" % name

#Ejercicio Mayuscula
def foor(name):
    return "Hi %s" % name.title()

#conversion 
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12

#conversion formato
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))

#conversio formato 3
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))