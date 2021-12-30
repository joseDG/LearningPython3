# Recall

tup = 1, 2, 3, 4, 5

# * => varying number
a, b, *c = tup      # 1, 2, [3, 4, 5]
*a, b, c = tup      # [1, 2, 3], 4, 5
a, *b, c = tup      # 1, [2, 3, 4], 5
a, *b, c, d = tup   # 1, [2, 3], 4, 5


def f(*args):   # receive varying arguments
    print(args)

f(1, 2, 3, 4, 5)    # (1, 2, 3, 4, 5)
f(tup)              # ((1, 2, 3, 4, 5),)
f(*tup)             # (1, 2, 3, 4, 5)