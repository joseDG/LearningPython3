
# please we wanna use math module
import math

print(math.sqrt(16))        # 4
print(math.factorial(5))    # 120
print(math.pi)              # 3.141592653589793
print(math.cos(math.pi/2))  # 0 - don't cos(90)

# More: Google python math module Or control over math

import math as XXX
print(XXX.pi)

from math import pi, factorial
print(pi)
print(factorial(5))

from math import *  # all is now visible: avoid