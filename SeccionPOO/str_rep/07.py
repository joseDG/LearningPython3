class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # intended for customers / goal: readable
        return "Employee " + self.name + " is " + str(self.age) + " years old"

    def __repr__(
        self,
    ):  # intended by developers e.g. for debugging/logging / goal: unambiguous
        return 'Employee(name="' + self.name + '", age=' + str(self.age) + ")"
        # observe: it is nice to use its output as a class object for debugging


most = Employee("mostafa", 33)

print(str(most))  # Employee mostafa is 33 years old
# if __str__ is provided, it will be used

print(repr(most))  # Employee(name="mostafa", age=33)
