
# list(iterable) = constructor
lst = list('mostafa')
print(len(lst))     # 7
print(lst)  # ['m', 'o', 's', 't', 'a', 'f', 'a']

new_lst = lst.copy()

print(lst is new_lst)   # False
# independent changes

print(new_lst is new_lst + [1])     # False