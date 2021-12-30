def check(m):
    import sys
    return str(m in sys.modules)

print(f"in top b.by: a {check('a')}")
print(f"in top b.by: b {check('b')}")

import a

x = 1
def bf():
    print(a.af())

print(f"in bottom b.by: a {check('a')}")
print(f"in bottom b.by: b {check('b')}")

