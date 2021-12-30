

def outer(x):
    y = 20
    print(id(y))

    def inner(f):
        print(id(y))
        return x + y + f

    return inner


if __name__ == '__main__':
    f = outer(10)
    print(f(30))  # 60: 10 + 20 + 30
    print(f(40))  # 70: 10 + 20 + 40

    print(outer(100)(5))    # 125


