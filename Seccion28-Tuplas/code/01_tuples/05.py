
class Employee:
    def __init__(self):
        self.id = 0


lst = [1, 2, 3, 4]
emp = Employee()

tu = (lst, emp)
print(tu[0])    # [1, 2, 3, 4]

# we can't change the items, but can change thier content if mutable
#tu[0] = [6, 7]  # TypeError
lst[0] = 100
emp.id = 20

print(tu[0])     # [100, 2, 3, 4]

