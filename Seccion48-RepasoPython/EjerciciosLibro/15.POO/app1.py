class Persona:

    #Creacion del constructor
    def __init__(self, nombre, apellido, edad):
        self.Nombre = nombre
        self.Apellidos = apellido
        self.Edad = edad 

    #Creacion Metodo
    def MostrarPersona(self):
        print("Nombre:" + self.Nombre)
        print("Apellidos: " + self.Apellidos)
        print("Edad: " + str(self.Edad))

print("OBJETOS ORIGINALES")
p1 = Persona("Alfredo","Moreno",35)
p1.MostrarPersona()

p2 = Persona("Valeria","Moreno", 25)
p2.MostrarPersona()

p1 = p2
print("OBJETOS TRAS ASIGNACION")
p1.MostrarPersona()
p2.MostrarPersona()

