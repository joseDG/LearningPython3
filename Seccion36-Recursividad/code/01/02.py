
def factorial1():
    return 1    #    base case. No subproblems

def factorial2():
    return factorial1() * 2


def factorial3():
    return factorial2() * 3


def factorial4():
    return factorial3() * 4


def factorial5():
    return factorial4() * 5


def factorial6():
    return factorial5() * 6


print(factorial6())

