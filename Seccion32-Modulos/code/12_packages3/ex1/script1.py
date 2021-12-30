print(dir())
# ['__file__', '__name__', ...]

from library import *
print(dir())
# ['__file__', '__name__', ..., 'backend', 'frontend']

from library.backend import *
print(dir())
# ['__file__', '__name__', ..., 'backend', 'frontend', 'utilities']

print(utilities.sq(5))
# Again: avoid import *
