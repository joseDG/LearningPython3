

def abs_sum(a, b, c):
    # we can define a nested (inner function)
    # hidden from the global scope (hidden)
    def my_abs(x):
        if x < 0:
            return -x
        return x

    return my_abs(a) + my_abs(b) + my_abs(c)

print(abs_sum(10, -20, 30)) # 60
#print(my_abs(10))  not defined
#abs_sum.my_abs  no attribute 'my_abs'

# But why doing so? Hiding?
# Better provide an outer function _my_abs