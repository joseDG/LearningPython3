
# support all the different ways of passing arguments

s = lambda *args: sum(args)
print(s(1, 2, 3))    # 6

res = (lambda **kwargs: sum(kwargs.values()))(A=1, B=2, C=3, D=4)
print(res)  # 10

# It access local and enclosing vars. Return as a closure
glob = 5
def f():
    x = 10
    fun = lambda y : y + x + glob

    return fun

fun = f()
print(fun(3))   # 18: 5+10+3

