
def fun():
    lst = []

    for i in range(3):
        def f(i = i):   # pass as default value
            return i
        lst.append(f)
    # all f captures var i (not value)
    # by end of fun(), i = 2
    return lst


lst = fun()
for f in lst:
    print(f())

"""
0
1
2
"""