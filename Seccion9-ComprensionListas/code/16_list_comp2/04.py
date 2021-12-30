

lst = [1, 3, 6, 7, 11, 15, -2]

def equ(i):
    return 2 * i

lst1 = []
for n in lst:
    res = equ(n)
    if res > 20:
        lst1.append(res)

print(lst1)     # [22, 30_oop]

lst2 = [equ(n)     for n in lst   if equ(n) > 20]
print(lst2)     # [22 30_oop]


# But this list Comprehension is slower!
# we called equ(n) twice!

