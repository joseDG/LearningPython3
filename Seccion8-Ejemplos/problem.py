def oraciones(frase):
    preguntas = ("how", "what", "why")
    capitalizar = frase.capitalize()
    if frase.startswitch(preguntas):
        return "{}?".format(capitalizar)
    else:
        return "{}.".format(capitalizar)

resultados = []

while True:
    usuario = input("Di algo: ")
    if usuario == "\end":
        break
    else:
        resultados.append(oraciones(usuario))

print(" ".join(resultados))