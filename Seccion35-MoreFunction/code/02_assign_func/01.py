


def fun(a, b):
    return a+b, a-b


if __name__ == '__main__':
    print(fun(10, 3))   # (13, 7)

    # function as variable name
    my_fun = fun
    print(my_fun(10, 3))  # (13, 7)

