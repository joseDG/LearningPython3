

# without
def add_value(lst_of_lists, value):
    # add the value to each item
    new_lst_of_lists = []
    for lst in lst_of_lists:
        new_lst = []
        for item in lst:
            new_lst.append(item + value)
        new_lst_of_lists.append(new_lst)
    return new_lst_of_lists

lst_of_lists = [[1, 2], [3], [4, 5, 6, 7, 8], [9, 10, 11]]

value = 10
print(add_value(lst_of_lists, value))
# [[11, 12], [13], [14, 15, 16, 17, 18], [19, 20, 21]]

# we get the lst, then transform it to a new list
lst_of_lists2 = [ [item+value for item in lst] for lst in lst_of_lists]
print(lst_of_lists2)
# [[11, 12], [13], [14, 15, 16, 17, 18], [19, 20, 21]]
