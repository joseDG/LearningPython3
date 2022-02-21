class Student:
    no_of_subjects = 10
    def __init__(self, name, marks, section):
        self.name = name
        self.amarks = marks
        self.asection = section

    def details(self):
        return f"Name is {self.name}, marks are {self.amarks} and section is {self.asection} "

    #Creacion de metodos estaticos
    @staticmethod
    def print_str(string):
        print("My name is "+ string)

a = Student("Seeta", 45, "B")
b = Student("Meera", 50, "C")

#Impirmir los estudiantes
a.print_str("Jose")
print(a.details())