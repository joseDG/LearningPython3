
my_list = [1, 5, 10, 17, 2, 'Hii']

# pop removes the item at a specific index and returns it.
print(my_list.pop())    # Hii  - default last item
# Now list is : 1 5 10 17 2

print(my_list.pop(3))    # 17
# Now list is : 1 5 10 2

# del removes the item at a specific index:
del my_list[0]  # 5 10 2

# remove removes the first matching value, not a specific index:
my_list.remove(10)  # 5 2

# ValueError: list.remove(x): x not in list
#my_list.remove('Hei')

for item in my_list:
    print(item, end=' ')
print()

