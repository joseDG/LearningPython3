

def f():
    from math import pi, factorial
    print(pi)
    print(factorial(5))

    #SyntaxError: import * only allowed at module level
    #from math import *

if __name__ == '__main__':
    f()