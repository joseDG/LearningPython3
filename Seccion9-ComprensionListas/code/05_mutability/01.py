# list is mutable

def f1(lst):
    # we can change + caller is changed
    lst[0] = 10

def f2(lst):
    lst = [7, 8, 9]     # local variable
    return lst


my_lst = [1, 2, 3, 4, 5]

another_lst = my_lst
print(another_lst is my_lst)    # True

f1(another_lst)
print(my_lst[0])    # 10 Change

f2(my_lst)
print(my_lst[1])    # 2  NO change

my_lst = f2(my_lst)      # replace
print(my_lst[1])         # 8 - new list
print(another_lst[1])    # 2 - no effect
