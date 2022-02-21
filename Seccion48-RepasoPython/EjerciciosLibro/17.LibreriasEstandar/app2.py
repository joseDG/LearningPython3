"""
MODULOS OS Y SHUTIL
modulos os nos permite interactuar con el sistema operativo y manejar
todas las funcionalidades que ofrece

getcwd: devuelve el directorio actual de trabajo de la aplicacion
chdir: cambia el directorio de trabajo
getpid: devuelve el identificado del proceso
getuid: devulve el identificador del usuario del proceso
"""
import os 
print("Directorio de trabajo actual:",os.getcwd())
os.chdir("/User/josh/Desktop/")
print("Nueva directorio de trabajo: ",os.getcwd())
print("ID del proceso: ", os.getpid())
print("ID del usuario del proceso: ", os.getuid())

"""
Utilizar modulos shutil que nospermite administrar ficheros de
forma sencilla
listdir:lista el contenido del directorio actual
mkdir:crea un nuevo directorio
rename:renombra el fichero
copy:realiza la copia del fichero
move:mueve el fichero especificado
"""
import os
import shutil
print("!Cambiando direcotrio de trabajo")
os.chdir("/Users/afre/Desktop/Ejercicio/")
print("Nuevo direcotrio de trabajo: ", os.getcwdb())
print("Contenido del directorio: ", os.listdir())
print("Copiando el fichero de prieba")
shutil.copy("prueba.txt","NuevaPrueba.txt")
print("Renombrado el fichero NuevaPrueba.txt!")
os.rename("NuevaPrueaba.txt","Ejercio.txt")
print("Contenido del directorio:", os.listdir())
print("Creando el nuvo directorio")
os.mkdir("NuevoDirectorio")