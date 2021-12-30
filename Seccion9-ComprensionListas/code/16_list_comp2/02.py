

lst = [1, -2, 6, -3, 2, -6]

def sq(i):
    return i * i

def is_even(i):
    return i % 2 == 0

lst5 = [sq(n) for n in lst   if is_even(n)]
print(lst5)     # [4, 36, 4, 36]


# we call if is_even(n) : filter
# we call sq(n)         : transform
