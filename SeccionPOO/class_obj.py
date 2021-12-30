class Employee:
    name = None
    salary = None
    address = None


jose = Employee()
jose.name = "Jose"
jose.salary = 100
jose.address = "Cuenca y Pasaje"

print(jose.name)
print(jose.salary)
print(jose.address)

emp2 = Employee()
emp2.name = "belal mostafa saad"
emp2.salary = 0
emp2.address = "Same as his dad"

print(emp2.address)  # Same as his dad
emp2.address = "BC"
print(emp2.address)  # BC

emp3 = Employee()
emp4 = Employee()
