class Animales():
    def __init__(self, nombre, mensaje):
        self.nombre = nombre
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


class Perro(Animales):
    def hablar(self):
        print("Yo hago Gauu")


class Pez(Animales):
    def hablar(self):
        print("Yo no hablo Boooo")


perro = Perro("Firulais", "Gua")
perro.hablar()

animales = [Perro("Firulais", "Guaa"), Pez("nemo", "nada")]
for i in animales:
    print(i.hablar())
