


def myfilter(func, iterable):
    return [item for item in iterable if func(item)]


def is_even(n):
    return n % 2 == 0


res = myfilter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6, 10, 13])

print(res)  # [2, 4, 6, 10]


