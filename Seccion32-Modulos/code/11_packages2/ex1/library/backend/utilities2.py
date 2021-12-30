# If u run utilities.py: it looks around for a parent package!
# ImportError: attempted relative import with no known parent package

# ..package: to access this sibiling-same level package
from ..frontend.web import f1
f1()

#from utilities1 import sq_f1   # Error
from .utilities1 import sq_f1   # .package same level as me
# from .. import frontend  ==> from parent dir import frontend
def sq_f2(n):
    return sq_f1(n) * n




from .sub import test