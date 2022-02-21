#importar la libreria para utilizar SQlite
import sqlite3

#conectar ala base de datos
database = sqlite3.connect("Coches.db")

#Crea los registros de fabricantes
register1 = (1, 'Honda', '911234567', 'Calle Japon 3','hello@hotmail.com')
register2 = (1, 'Seat', '911234585', 'Calle Espana 1','car@hotmail.com')

#Apertura de un cursor e insercion de los fabricantes
cursor = database.cursor()
cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register1)
cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register2)

#Commit de las operaciones
database.commit()

#Crea los registros de los coches
register1 = (1,1,'Civic',1600,'Azul')
register2 = (1,1,'HR-V',2400,'Negro')
register3 = (1,1,'Ibiza',1800,'Rojo')
register4 = (1,1,'Ateca',1900,'Blanco')

#Insercion de los modelos de coches
cursor.execute("INSERT OR IGNORE INTO Coche VALUES(?,?,?,?,?)", register1)
cursor.execute("INSERT OR IGNORE INTO Coche VALUES(?,?,?,?,?)", register2)
cursor.execute("INSERT OR IGNORE INTO Coche VALUES(?,?,?,?,?)", register3)
cursor.execute("INSERT OR IGNORE INTO Coche VALUES(?,?,?,?,?)", register4)

#Commit de las operaciones
database.commit()

#Cierra la conexion a la base de datos
database.close()