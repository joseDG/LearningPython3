class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Employee " + self.name + " is " + str(self.age) + " years old"


most = Employee("mostafa", 33)

print(repr(most))  # <__main__.Employee object at 0x7f574a93fb90>

# if __repr__ is not provided, __str__ is NOT used
# # Almost every object you implement should have __repr__
