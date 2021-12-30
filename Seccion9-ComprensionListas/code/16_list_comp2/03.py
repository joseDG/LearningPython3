

x = 10
m = x if x % 2 == 0 else 2 * x
print(m)    # 10

x += 1
m = x if x % 2 == 0 else 2 * x
print(m)    # 22

lst1 = [1, 2, 3, -4, 5, -6, 7, 8]
lst2 = [n for n in lst1 if n % 2 == 0]
print(lst2)     # [2, -4, -6, 8]

lst3 = [n if n > 0 else -n   for n in lst1 if n % 2 == 0]
print(lst3)     # [2, 4, 6, 8]

# we can replace these 2 if with functions
