class Persona():

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print("El objeto {} {} ha sido creado".format(
            self.nombre, self.apellido))
