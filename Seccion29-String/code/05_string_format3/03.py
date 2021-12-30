
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Employee {self.name} is {self.age} years old'

    def __repr__(self):
        return f'Employee(name="{self.name}", age={self.age})'

most = Employee('mostafa', 33)
print(f'{most}')        # Employee mostafa is 33 years old
# add !r to use the dunder repr
print(f'{most!r}')      # Employee(name="mostafa", age=33)

print(f"{2 * 3+ 1}")    # 7
name = 'mostafa'
print(f"{name.lower()} has udemy courses")  # mostafa has udemy courses

