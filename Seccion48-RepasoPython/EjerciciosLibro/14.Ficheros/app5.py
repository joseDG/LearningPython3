from cgitb import text


print("FICHERO INICIAL")
flectura = open("fichero.txt","r")
texto = flectura.read()
flectura.close()
print(texto)
print("INSERTANDO LINEA....\n")
frescritura = open("fichero.txt","a")
frescritura.write("Nueva linea en el fichero\n")
frescritura.close()
print("FICHERO INCIAL")
flectura = open("fichero.txt","r")
texto = flectura.read()
flectura.close()
print(texto)
