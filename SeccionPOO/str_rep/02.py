class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Employee " + self.name + " is " + str(self.age) + " years old"


most = Employee("mostafa", 33)

print(most)  # Employee mostafa is 33 years old
s = str(most)  # Employee mostafa is 33 years old

print(
    most.__str__()
)  # Employee mostafa is 33 years old      # you shouldn't call. use str()
