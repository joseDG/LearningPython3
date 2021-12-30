import ourlib

print(ourlib.sq(5))     # 25


import sys
sys.path.append('somewhere/mycode')     # bad / (linux) not windows

import mymath   # now is visible on the path
print(mymath.sum1n(5))      # 15


# Note: sometimes u want to add in the top of the list