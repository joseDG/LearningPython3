

def fib(n):
    print(n)
    if n <= 1:
        return 1

    return fib(n-1) + fib(n-2)



if __name__ == '__main__':
    print(fib(50))
    print(fib(35))  # 14930352
    print(fib(50))  # Hmmmm