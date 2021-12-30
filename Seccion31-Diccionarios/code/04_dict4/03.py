
# most common
a = {'one': 1, 'two': 2, 'three': 3}
# constructor: pass dict as an argument
b = dict({'three': 3, 'one': 1, 'two': 2})
# from list of tuples: key/value
c = dict([('two', 2), ('one', 1), ('three', 3)])
# Use keyword arguments
d = dict(one=1, two=2, three=3)
# From a dictionary, followed by keywords
e = dict({'one': 1, 'three': 3}, two=2)
# zip on 2 lists used as key/value
f = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

print(a == b == c == d == e == f)


