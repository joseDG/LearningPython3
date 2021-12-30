

my_list = [1, 2, 3, 4]

print(len(my_list))     # 4

print(2 in my_list)     # True
print(9 in my_list)     # False

for item in my_list:    # 1 2 3 4
    print(item, end=' ')
print()

print(my_list)  # [1, 2, 3, 4]

# list of different data types!
my_list = [1, 'mostafa', 4.5]

# IndexError: list assignment index out of range
#my_list[3] = 0