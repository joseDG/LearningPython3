

def add(x: float, y: float) -> float:
    print(add.__annotations__)
    # {'x': <class 'float'>, 'y': <class 'float'>, 'return': <class 'float'>}
    return x + y


print(add(2, 7))        # 9
print(add('2', '7'))    # 27


def mylist(x: str, y) -> list:
    # variable type
    z : str = x + y
    res : list = [x, y, z]

    print(mylist.__annotations__)
    # {'x': <class 'str'>, 'return': <class 'list'>}

    return res

mylist(10, 20)


