

def outer():
    outer_loc1 = 30 # for inner func: this is an enclosing scope

    def inner():
        print(outer_loc1)   # 30: local? No. Enclosing? Yes, use it
    inner()

outer()

"""
But how python searches for variable?
We learned before about local, global and built-in
"""
