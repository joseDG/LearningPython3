

def factorial(n):
    res = 1

    for i in range(2, n+1):
        res *= i

    return res


if __name__ == '__main__':
    print(factorial(3))     # 1 * 2 * 3
    print(factorial(4))     # 1 * 2 * 3 * 4

    print(factorial(5))     # 1 * 2 * 3 * 4 * 5
                            # factorial(4)  * 5 = 120

    print(factorial(6))     # 1 * 2 * 3 * 4 * 5 * 6 = 720
                            # factorial(5)      * 6 = 720
                            # factorial(4)  * 5 * 6 = 720
                            # factorial(3)*4* 5 * 6 = 720
    

