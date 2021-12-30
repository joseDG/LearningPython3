

print(dir())    # dir() returns a list of defined names in a namespace
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

import ourlib
print(dir())
# ['__annotations__', '__builtins__', ... 'ourlib']

print(dir(ourlib))
# [, 'sq', 'sum1n']

from ourlib import sq
print(dir())
# ['__annotations__', '__builtins__', ... 'ourlib', 'sq']

from ourlib import *
print(dir())
# ['__annotations__', '__builtins__', ... 'ourlib', 'sq', 'sum1n']