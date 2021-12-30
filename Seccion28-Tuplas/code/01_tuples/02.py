

# creation
t = ('mostafa', 12, 2.5, 12)    # 4 items!
t = ('mostafa', 12, 2.5, 12, )  # also 4 items!

t = (10)
print(type(t))  # SADLY int not tuple :(
t = (10, )      # tuple of 1 item
t = ()          # tuple of 0 item

print(len((True, 'mostafa')))     # 2

# all are tuples
x, y = 1, 2
x, y = (1, 2)
(x, y) = (1, 2)

# TypeError: tuple expected at most 1 arguments, got 3
#t = tuple(1, 2, 3)
t = tuple((1, 2, 3))    # constructor: iterable
t = tuple([1, 2, 3])
t = tuple('most')       # ('m', 'o', 's', 't')

