

def fun():
    fun.counter += 1
    print(fun.counter)

print(type(fun))  # <class 'function'>

# everything in python is object: so function var is an object!
# this means it has attributes!

print(fun.__dict__) # {}
fun.counter = 0

fun()   # 1
fun()   # 2
fun()   # 3

# we typically don't do that, just to administrate the idea!

