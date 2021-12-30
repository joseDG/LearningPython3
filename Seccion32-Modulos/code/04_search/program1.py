import ourlib

print(ourlib.sq(5))     # 25


# ModuleNotFoundError: No module named 'mymath'
import mymath
print(mymath.sum1n(5))

# mymath is not visible
# neither on script directory (04_search)
# nor on pythonpath nor installation dirs!

# one way: let's add to sys.path