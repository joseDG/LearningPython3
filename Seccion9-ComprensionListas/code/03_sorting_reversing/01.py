
lst = [5, 7, 2]
# NO new list: in-place - memory efficient
lst.sort()                  # [2 5 7]

lst.sort(reverse=True)      # [7 5 2]

# common mistake:
lst = lst.sort()
# lst now is NONE!

lst = [5, 7, 2]
lst_sorted_cpy = sorted(lst)    # sorted copy
# lst = NO CHANGE
# lst_sorted_cpy [2 5 7]

my_str = 'zacb'
new_lst = sorted(my_str)    # LIST! ['a', 'b', 'c', 'z']
new_lst = sorted(my_str, reverse=True)
# new_lst = ['z', 'c', 'b', 'a']

print(new_lst)
# common mistake
sorted = sorted(my_str)
# now sorted become a variable. You can't call the function
# TypeError: 'list' object is not callable
#sorted = sorted(my_str)