class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Employee " + self.name + " is " + str(self.age) + " years old" + " **"


most = Employee("mostafa", 33)

print(most)  # Employee mostafa is 33 years old **

# if __str__ is not provided, __repr__
# then __repr__ is used

print(str(most))  # Employee mostafa is 33 years old **
print(repr(most))  # Employee mostafa is 33 years old **
