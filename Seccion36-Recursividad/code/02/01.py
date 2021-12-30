
def factorial(n):
    print("Function Call: factorial: n=", n)

    if n == 1:      # base case
        return 1
    subproblem = factorial(n-1)
    return subproblem * n


print(factorial(6))


