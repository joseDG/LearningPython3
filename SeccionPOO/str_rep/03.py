class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name, self.age


most = Employee("mostafa", 33)

print(most.__str__())  # ('mostafa', 33)

# TypeError: __str__ returned non-string (type tuple)
print(str(most))  # it must return string
