class Persona():
    nombre: "Carlos"
    apellido: "Vergara"
    sexo: "Masculino"
    edad: 39

    def hablar(self, mensaje):
        return mensaje


persona = Persona()

persona.nombre
persona.apellido
persona.sexo
persona.edad

print(persona.hablar("Hola Soy"), "{} y mi apellido es {}, tengo {} y de sexo {}".format(
    persona.nombre, persona.apellido, persona.edad, persona.sexo))
