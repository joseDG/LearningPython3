def check(m):
    import sys
    return str(m in sys.modules)

print(f"in top a.by: a {check('a')}")
print(f"in top a.by: b {check('b')}")

import b
def af():
    return b.x
af()

print(f"in bottom a.by: a {check('a')}")
print(f"in bottom a.by: b {check('b')}")

