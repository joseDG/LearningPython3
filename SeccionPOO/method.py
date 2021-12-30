class Employee:
    name = None
    salary = None
    address = None


# Function takes object
# print using .
def print_empl(object):
    print("Employee name:", object.name)
    print("Employee salary:", object.salary)
    print("Employee address:", object.address)


x = 1
mostafa = Employee()
mostafa.name = "mostafa saad"
mostafa.salary = 1000
mostafa.address = "Lovely Canada"

print_empl(mostafa)
