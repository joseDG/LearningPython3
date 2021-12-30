

class Employee:
    def __init__(self):
        self.id = 10
    def __repr__(self):
        return str(self.id)
emp = Employee()
lst = [5, 8, 9]
dict = {'ziad' : 25.5, 2 : lst, 'Hey' : emp}
print(dict) # {'ziad': 25.5, 2: [5, 8, 9], 'Hey': 10}

lst.pop()
emp.id += 100
print(dict) # {'ziad': 25.5, 2: [5, 8], 'Hey': 110}

lst = [5]
print(dict) # {'ziad': 25.5, 2: [5, 8], 'Hey': 110}
d2 = dict.copy()
print(d2['Hey'] is emp) # True - shallow copy