
# Recall: expression => evalautes to a value
    # 2 * x + 1, x * x, x == 2, somefun(.)

# statement doesn't necessairly
    # x = 2, assert x == 2, etc
    # In python 2: print was a statement

# lambda allows 1 single expression (could long / multiline)
    # It doesn't allow statements

#f = lambda x: assert x == 2 # invalid syntax

f = lambda x : print(x, x*x, 2*x)   # return None


print(f(5))
# 5 25 10
# None