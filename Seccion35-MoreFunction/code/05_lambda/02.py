
def process1(iterable, fun):
    """Iterate on the iterable, apply function and reutmr sum"""
    sum = 0
    for value in iterable:
        sum += fun(value)

    return sum

process2 = lambda iterable, fun: sum([fun(value) for value in iterable])

lst = [2, -4, 6]

print(process1(lst, abs))    # 12
print(process2(lst, abs))    # 12

print(process2(lst, lambda x: x * x))    # 56



