
def fun():
    lst = []

    for i in range(3):
        def f():
            return i
        lst.append(f)
    # all f captures var i (not value)
    # by end of fun(), i = 2
    return lst


lst = fun()
for f in lst:
    print(f())

"""
2
2
2
"""