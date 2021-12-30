
my_list = [1, 2, 3, 4]

my_list.reverse()   # 4 3 2 1

my_list += ['Hi']

new_lst = reversed(my_list)
print(new_lst)  # list_reverseiterator

new_lst_rev1 = list(reversed(my_list))
print(new_lst_rev1)  # list_reverseiterator
# ['Hi', 1, 2, 3, 4]

new_lst_rev2 = my_list.copy()
new_lst_rev2.reverse()
print(new_lst_rev2)
# ['Hi', 1, 2, 3, 4]
