
# If u run utilities.py: it looks around for library.backend
# but it won't find it!
# ModuleNotFoundError: No module named 'library'
# Review: Module search path in sys.path

# This line will work well ONLY when u run script1 itself!
from library.frontend.web import f1

# If urgent workaround, you may add whatever in sys.path

def sq_f1(n):
    f1()
    return n*n



