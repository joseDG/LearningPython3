
tup = 1, 2, (5, 6)

#ValueError: not enough values to unpack (expected 4, got 3)
#a, b, c, d = lst

print(len(tup)) # 3

# deep unpacking
a, b, (c, d) = tup
print(a, b, c, d)   # 1 2 5 6

t = 1, 2, 3, (4, (5, 6))
a, b, c, (d, (e, f)) = t
print(a, b, c, d, e, f) # 1 2 3 4 5 6

