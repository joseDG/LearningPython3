fcrear = open("ficheronuevo.txt","w")
fcrear.write("Fichero creado desde cero \n")
fcrear.write("Lorem ipsum dolo sit amet, consectuar adipsi alit,")
fcrear.write("Lorem ipsum dolo sit amet, consectuar adipsi alit,")
fcrear.write("Lorem ipsum dolo sit amet, consectuar adipsi alit,")
fcrear.write("Lorem ipsum dolo sit amet, consectuar adipsi alit,")
fcrear.write("Lorem ipsum dolo sit amet, consectuar adipsi alit,asdfasdf")
fcrear.close()

print("### Fichero crando ###")

flectura = open("ficheronuevo.txt","r")
texto = flectura.read()
flectura.close()
print(texto)