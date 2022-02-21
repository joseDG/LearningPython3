"""
NOTE
Exception => tipo de excepcion mas generica
AritmeticEror => tipo de excepciones ariemticos
BufferError => tipo de excepcion generica BUFFERS
LookupError => tipo de excepcion generica para errores con BD
"""

print("!Iniciando programa!")
print("\n!Comenzando primera parte del programa")
try:
    print(str(17/0))
except:
    print("ERROR: Division por cero")
finally:
    print("Primera parte de programa acabaria")


print("!Comenzando segundo parte del programa")
try:
    print(str(17/1))
except:
    print("ERROR: Division por cero")
finally:
    print("Segunda parte de programa acabada")

print("Iniciando programa")
try:
    print(str(17/1))
except ZeroDivisionError:
    print("ERROR: Division por cero")
except:
    print("Error: General")
else:
    print("No se han producido errores")
finally:
    print("Programa acabado")