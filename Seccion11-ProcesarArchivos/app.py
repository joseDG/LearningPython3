# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()

# with open("files/vegetales.txt", "w") as myfile:
#     myfile.write("Tomato\nCumcuber\nOnion")
#     myfile.write("Gralic")
#     #content = myfile.read()

with open("files/fruits.txt", "a+") as myfile:
    myfile.write("\nOkra")
    #deja un espacio
    myfile.seek(0)
    content = myfile.read()

print(content)

#ejercico
# def foo(character, filepath="bear.txt"):
   # file = open(filepath)
    #content = file.read()
    #return content.count(character)

#ejercico
# with open("file.txt", "w") as file:
    # file.write("snail")

#ejercicio
# with open("bear.txt") as file:
#     content = file.read()

# with open("first.txt", "w") as file:
    # file.write(content[:90])

with open("bear1.txt") as file:
    content = file.read()

with open("bear2.txt", "a") as file:
    file.write(content)

#ejercicios
with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

