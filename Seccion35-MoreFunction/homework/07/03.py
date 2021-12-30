

def myreduce(func1_overall, func2_consecutive, iterable):
    try:
        first, second, *iterable = iterable
        res = func2_consecutive(first, second)
    except:
        return RuntimeError('The length of the sequence must be at least 2')

    while iterable:
        try:
            first, second, *iterable = iterable
        except:
            return RuntimeError('The length of the sequence must be even')
        res = func1_overall(res, func2_consecutive(first, second))
    return res


print(myreduce(lambda a, b: a * b, lambda a, b: a + b, [2, 5, 3, 4, 5, 10]))

