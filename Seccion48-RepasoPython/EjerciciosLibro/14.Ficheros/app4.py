f = open("fichero.txt","r")
lineas = list(f)
f.close()
for item in lineas:
    print(item)