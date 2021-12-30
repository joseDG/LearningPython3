

my_list = [1, 15, 7, 'mostafa', 7, True, 0]

# search and return the FIRST index
print(my_list.index(7))         # 2
print(my_list.index('mostafa')) # 3
print(my_list.index(True))      # 0 **
print(my_list.index(False))     # 6 **

#ValueError: 'Wow' is not in list
#print(my_list.index('Wow'))

my_list.clear()
print(len(my_list))     # 0
