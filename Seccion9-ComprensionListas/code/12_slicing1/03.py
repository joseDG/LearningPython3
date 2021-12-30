
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

sub_list = my_list[0:5]  # 0 1 2 3 4
# If you did not provide start: then 0
sub_list = my_list[ :5]  # 0 1 2 3 4

# 9 = len(my_list)
sub_list = my_list[4:9]  # 4 5 6 7 8
# similarly: if not end: it is len
sub_list = my_list[4: ]  # 4 5 6 7 8

# observe:
# my_list[4] is the 5th element (index 4)
# my_list[4:] is slice from index 4 to last element
# my_list[:4] is slice from 0 to 3

same_values = my_list[:4] + my_list[4:]
# 0 1 2 3 4 5 6 7 8
print(same_values is my_list)   # False

# both start and end are empty: WHOLE list
same_values = my_list[:]

print(same_values)