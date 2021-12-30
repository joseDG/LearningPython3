

def f(a, b, *myargs, **mykwargs):
    print(a, b, 'args', myargs, 'kwargs', mykwargs)


f(1, 2)             # 1 2 args () kwargs {}

f(a=10, b=20)       # 10 20 args () kwargs {}

#f(x=10, y=20)
# TypeError: f() missing 2 required positional arguments: 'a' and 'b'

f(1, 2, x=10, y=20) # 1 2 args () kwargs {'x': 10, 'y': 20}

f(1, 2, 3, 4, 5, x=10, y=20)   # 1 2 args (3, 4, 5) kwargs {'x': 10, 'y': 20}

#f(a=1, b=2, a=10, b=20)  # SyntaxError: keyword argument repeated

# Order: Standard arguments, *args arguments, **kwargs arguments
