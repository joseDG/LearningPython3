
st1 = {1, 5}
st2 = {2, 1, 5, 3}

# True if every element of st1 is in st2
print(st1 <= st2)           # True
print(st1.issubset(st2))    # True

# True if every element of st1 is in st2, but not equal
print(st1 < st2)            # True
print(st1 < {1, 5})         # False

print(st2 >= st1)             # True
print(st2.issuperset(st1))    # True
print(st1 >= {1, 5})          # True
print(st1 > {1, 5})           # False
