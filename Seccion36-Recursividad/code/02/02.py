
def factorial(n):
    print("Function Call: factorial: n=", n)

    return factorial(n-1) * n


print(factorial(6))


