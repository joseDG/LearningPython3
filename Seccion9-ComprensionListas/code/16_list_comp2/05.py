

# Walrus Operator: Python 3.8
# Assignment expressions allow you to
# assign and return a value in the same expression

# assign status to True => return it
# print(status = True)   # Error
print(status := True)


if (sz := len('mostafa')) > 3:
    print(sz)  # 7

if sz:= len('mostafa') > 3: # without paranthese > evaluated first to if sz := True
    print(sz)  # True      Oops: be careful!

lst = [1, 3, 6, 7, 11, 15, -2]

def equ(i):
    return 2 * i

# When the condition will be evalauted, the variable name will be assigned
# Then we append directly in the list without recomputing it
lst3 = [ans for n in lst if (ans := equ(n)) > 20]
print(lst3)  # [22, 30_oop]

