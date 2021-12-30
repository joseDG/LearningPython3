
# Indexing and Slicing

s1 = 'moST'

print(s1[0], s1[-1])  # m T

print(s1[2:])    # ST
print(s1[::])    # moST
print(s1[::-1])  # TSom

#TypeError: 'str' object does not support item assignment
#s1[0] = 'c'

#TypeError: 'str' object doesn't support item deletion
#del s1[0]

