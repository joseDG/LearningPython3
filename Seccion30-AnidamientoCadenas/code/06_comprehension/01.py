

lst_of_lists = [[1, 2], [3], [4, 5, 6, 7, 8], [9, 10, 11]]

# Flatten a list: make all the items in a single list with no inner list
# we can do that easily with list comprehension

# without comprehension
lst1 = []
for lst in lst_of_lists:
    for item in lst:
        lst1.append(item)

print(lst1)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lst2 = [item for lst in lst_of_lists for item in lst]
# same list!

