class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print("El objeto {} {} ha sido creado".format(
            self.nombre, self.apellido))

    def __str__(self):
        print("El objeto {} {} ha sido destruido".format(
            self.nombre, self.apellido))

    def __del__(self):
        print("El objeto {} {} ha sido detruido".format(
            self.nombre, self.apellido))


persona = Persona("Walter", "Coto")
print(str(persona))
