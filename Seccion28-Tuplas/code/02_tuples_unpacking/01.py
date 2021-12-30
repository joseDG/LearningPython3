
tup = 1, 2, 3, 4, 5
a, b, c, d, e = tup     # normal unpacking
a, _, _, _, _ = tup     # what If i don't care? use _ a common notation

# what if I am not sure from the total number? use *
    # * here refers to varying number of arguments
a, b, *c = tup
print(c)    # [3, 4, 5]

*a, b, c = tup
print(a)    # [1, 2, 3]

a, *b, c = tup
print(b)    # [2, 3, 4]

a, *b, c, d = tup
print(b)    # [2, 3]

# Although we can do the same with slicing
# but the * operator is more elegant and makes code simpler!

def f(*items):
    print(items)  # (1, 2, 3, 4)

f(1, 2, 3, 4)