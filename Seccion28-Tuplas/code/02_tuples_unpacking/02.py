# * unpacking operator

lst = [1, 2, 3]
print(lst)      # [1, 2, 3]
print(*lst)     # 1 2 3   unpack first, then print: print received 3 arguments NOT 1


def f(a, b):
    print(a+b)

#f(*lst)    f() takes 2 positional arguments but 3 were given

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
conc = [*lst1, *lst2]
print(conc) # [1, 2, 3, 4, 5, 6]

