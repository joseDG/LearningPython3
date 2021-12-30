
# same rules as string comparison
    # Item by item comparison
        # if an item is smaller, its list is smaller
        # if one list ended, it is the sammer
lst1 = [1, 5, 8]
lst2 = [1, 5, 8]
lst3 = [1, 5]
lst4 = [7, 5]
print(lst1 is lst2)     # False (must)
print(lst1 == lst2)     # True

print([1, 2, 3] is [1, 2] + [3])    # False (must)
print([1, 2, 3] == [1, 2] + [3])    # True


print(lst1 < lst2)      # False
print(lst1 <= lst2)     # True
print(lst1 <= lst3)     # False
print(lst1 <= lst4)     # True

# TypeError: '<' not supported between instances of 'int' and 'str'
#print([1, 2] < ['mostafa'])
