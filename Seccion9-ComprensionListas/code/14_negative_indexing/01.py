
       #  -7  -6 -5 -4 -3 -2 -1    # 7 + neg_pos
my_list = [0, 1, 2, 3, 4, 5, 6]

ln = len(my_list)

print(my_list[ln-1])    # 6 = last number
print(my_list[ln-2])    # 5 = 2nd last number

# Negative indexing
print(my_list[-1])    # 6 = last number
print(my_list[-2])    # 5 = 2nd last number

print(my_list.pop(-1))  # 6
print(my_list.pop(-1))  # 5

#my_list: [0, 1, 2, 3, 4]

