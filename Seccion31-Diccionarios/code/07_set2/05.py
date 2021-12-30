

# immutable set
st1 = frozenset([7, 5, 1, 8])
# can't change it: no add/remove etc

print(id(st1))  # 0x111
st1 |= {20, 10}
print(id(st1))  # 0x222 DIFFERENT - recall strings!

# useful if u need a set, but immutable
dct = {st1 : 5}

for item in sorted(st1):
    print(item, end=' ')
    # 1 5 7 8 10 20