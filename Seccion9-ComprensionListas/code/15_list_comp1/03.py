
lst1 = [1, -2, 6, -3, 2, -6]

# Old syntax
lst2 = []
for n in lst1:
    if n > 0:
        lst2.append(n)

print(lst2)     # [1, 6, 2]

# New syntax
lst3 = [n for n in lst1   if n > 0]
print(lst3)     # [1, 6, 2]

