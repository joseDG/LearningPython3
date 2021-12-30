

st = {1, 5, 1, 3, 5}
print(st)   # {1, 3, 5}

st = set(['saad', 'most', 'saad'])  # takes iterable

print('al' in st)       # False
for item in st:         # No guarantee on order
   print(item, end=' ') # most saad
print()

print(list(st))     # ['most', 'saad']
print(set({1:10, -2:30}))   # {1, -2}

print(set('Hey'))       # {'H', 'y', 'e'}
print(set(['Hey']))     # {'Hey'}
print(set({'Hey'}))     # {'Hey'}