
def process(iterable, fun):
    """Iterate on the iterable, apply function and reutmr sum"""
    sum = 0
    for value in iterable:
        sum += fun(value)

    return sum

lst = [2, -4, 6]

print(process(lst, abs))    # 12

def sq(n):
    return n*n

print(process(lst, sq))     # 56

funcs = [abs, sq]   # list of functions
for f in funcs:
    print(process(lst, f))
