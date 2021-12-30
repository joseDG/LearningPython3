

lst1 = [2, 3, 4, 1]

# Old syntax
lst2 = []
for i in lst1:
    lst2.append(i *i + 1)

print(lst2)     # [5, 10, 17, 2]

# new syntax
lst2 = [i*i+1   for i in lst1]
print(lst2)     # [5, 10, 17, 2]
