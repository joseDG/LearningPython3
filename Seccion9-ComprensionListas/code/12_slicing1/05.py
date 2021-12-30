

class Employee:
    pass

obj1 = Employee()
obj2 = Employee()
obj3 = Employee()

lst1 = [obj1, obj2, obj3]
lst2 = lst1[0:2]    # create a NEW list

print(lst1 is lst2)         # False
print(lst1[0] is lst2[0])   # True

# List is new - items are just assigned (same memory)

