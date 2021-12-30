

# new_list = [expression  for member in iterable   ]

lst1 = [2, 3, 4, 1]

lst2 = [i*i+1   for i in lst1]
print(lst2)     # [5, 10, 17, 2]

lst3 = [n+1 for n in range(5, 9)]
print(lst3)     # [6, 7, 8, 9]

lst4 = [3*char for char in 'Hey']
print(lst4)     # ['HHH', 'eee', 'yyy']

