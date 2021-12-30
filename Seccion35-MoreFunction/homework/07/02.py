

def myreduce(func, iterable, init = None):
    if not iterable:
        if init is None:
            raise TypeError('reduce of empty sequence with no initial value')
        return init

    for item in iterable:
        if init is None:
            init = item
        else:
            init = func(init, item)
    return init

print(myreduce(max, {7, 20, 10}))   # 20


print(myreduce(lambda a, b: a if a > b else b, {7, 20, 10}))


# Our myreduce definition is limited as it implies None can't be in the list nor as default value!
# There are ways to handle that, but let's keep it simple