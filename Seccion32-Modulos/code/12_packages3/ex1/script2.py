print(dir())
# ['__file__', '__name__', ...]

from library.frontend.web import *
print(dir())
# ['__file__', '__name__', ..., , 'f1', 'f2']

f2()    # 2

#NameError: name 'f3' is not defined
#f3()