
my_list = [1, 5, 10, 17, 2]

# append: add item to the end
my_list.append('Hii')   # 1 5 10 17 2 Hii

# Extend the list by appending all the items from the iterable
another_lst = [3, 1]
my_list.extend(another_lst)
# 1 5 10 17 2 Hii 3 1

#TypeError: 'int' object is not iterable
#my_list.extend(2)

# Insert an item at a given position
my_list.insert(2, 'Wow')
# 1 5 Wow 10 17 2 Hii 3 1

for item in my_list:
    print(item, end=' ')
print()
