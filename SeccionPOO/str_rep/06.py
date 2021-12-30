class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Employee " + self.name + " is " + str(self.age) + " years old"

    def __repr__(self):
        return "Employee " + self.name + " is " + str(self.age) + " years old" + " **"


most = Employee("mostafa", 33)

print(str(most))  # Employee mostafa is 33 years old
# if __str__ is provided, it will be used

print(repr(most))  # Employee mostafa is 33 years old **
