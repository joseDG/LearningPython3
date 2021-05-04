#Ejemplo de Listas

seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)

seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.4534345567)
seconds.remove(1.10001399445)
seconds.remove(1.023458894)

#Accediendo a los items
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])

#Slicing
sl = ['abc' , 'def', 'ghi', 'jkl', 'mno'][-2][-2]
print(sl)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])

#Conversion
#tupla a list
data = (1, 2, 3)
list(data)
[1, 2, 3]

#list a tupla
data = [1, 2, 3]
tuple(data)
(1, 2, 3)

#list a dictioanry
data = [["name", "John"], ["surname", "smith"]]
dict(data)
{'name': 'John', 'surname': 'smith'}

#Las listas, cadenas y tuplas tienen un sistema de índice positivo:
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6

#y un sistema un negativo index 
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1

#In a list, the 2nd, 3rd, and 4th items can be accessed with:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']

#primeros 3 dela lsita
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 

#ultimos 3 de la lsita
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']

#todos menos el ultimo
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

#todos menos los 2 ultimos
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

#unico diccionario puede acceder usando llaves
phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'