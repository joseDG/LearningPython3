

def f(*args, **kwargs):
    print('args', args, 'kwargs', kwargs)


f(1, 2)             # args (1, 2) kwargs {}

f(a=10, b=20)       # args () kwargs {'a': 10, 'b': 20}

f(1, 2, a=10, b=20) # args (1, 2) kwargs {'a': 10, 'b': 20}

#f(a=10, 1)  # CE positional argument follows keyword argument

#def f(**kwargs, *args):    # wrong

