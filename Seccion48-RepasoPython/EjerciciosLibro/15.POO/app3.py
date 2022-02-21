from xml.dom.minidom import Notation


#NOTA Crear encapsulacion
#Proteger datos o usos controlados
#Publicos datos accesibles sin control
#Privados datos que no pueden ser accesibles sin control
#Protect acceso conla clase hija
#Se aplican en atributos y metodos
#clases privadas se utilizan los metods GET & POST

class PersonaPublica:
    def __init__(self,nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad #public
        _prot = 4 #protect

class PersonaPrivada:
    def __init__(self, nombre, apellidos, edad):
        self.__Nombre = nombre
        self.__Apellidos = apellidos
        self.__Edad = edad#private

    def GetNombre(self):
        return self.__Nombre

    def GetApellidos(self):
        return self.__Apellidos

    def GetEdad(self):
        return self.__Edad


    def SetNombre(self, nombre):
        self.__Nombre = nombre

    def SetApellidos(self, apellidos):
        self.__Apellidos = apellidos

    def SetNombre(self, edad):
        self.__Edad = edad


publico = PersonaPublica("Alfredo","Moreno",35)
privado = PersonaPrivada("Valeria","Moreno",1)
print("PERSONA PUBLICA")
print("Nombre: " + publico.Nombre)
print("Nombre: " + publico.Apellidos)
print("Nombre: " + str(publico.Edad))

print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))

print("\nModificaicon de valores en ambos objetos")
publico.Apellidos = "Moreno Corcoles"
privado.SetApellidos("Moreno Munoz")

print("PERSONA PUBLICA")
print("Nombre: " + publico.Nombre)
print("Apellidos: " + publico.Apellidos)
print("Edad: " + str(publico.Edad))

print("PERSONA PRIVADA")
print("Nombre: " + privado.GetNombre())
print("Apellidos: " + privado.GetApellidos())
print("Edad: " + str(privado.GetEdad()))