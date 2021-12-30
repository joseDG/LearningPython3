

t1 = (1, 2, 3)
t2 = ('mostafa', True)

t = t1 + 2 * t2

print(t)
# (1, 2, 3, 'mostafa', True, 'mostafa', True)

# TypeError: can only concatenate tuple (not "list") to tuple
#t = t1 + [2, 3, 4]

print(('Hi') * 4)    # HiHiHiHi
print(('Hi',) * 4)   # ('Hi', 'Hi', 'Hi', 'Hi')

