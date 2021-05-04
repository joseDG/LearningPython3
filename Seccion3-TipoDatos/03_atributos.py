#El atributo para saber que metodos 
#pueda o requiera utilziar ne python son
#utilizando se coloca utilizando en la terminal python3 dir()

dir()

students_grades = [9.1,8.8,7.5]

mysum = sum(students_grades)
length = len(students_grades)
media = mysum / length

print(media)

#este algoritomo me permite buscar
#cuantos numeros 10.0 tengo
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

#Utilizacion de metodo para mayusculas
username = "Python3"
print(username.upper())