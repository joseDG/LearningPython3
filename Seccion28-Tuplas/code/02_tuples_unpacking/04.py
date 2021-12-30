
def f():
    return ((10, 20), (30, 40))

(x, y), (w, z)  = f()
print(w)    # 30_oop

all = f()
print(all)          # ((10, 20), (30_oop, 40))
sub = all[0]        # (10, 20)
print(sub[1])       # 20
print(all[0][1])    # 20
print(f()[0][1])    # 20

