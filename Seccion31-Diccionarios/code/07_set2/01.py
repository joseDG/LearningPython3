
st1 = {1, 5, 7, 8}
st2 = {1, 5, 3, 10}

print(st1 | st2)        # {1, 3, 5, 7, 8, 10}: union using | operator
print(st1.union(st2))   # same
print(st1.union([1, -5, -7]))   # pass any iterable
# note: st1 is not updated

st3 = {5, 6, 1}
su = st1 | st2 | st3
si = st1 & st2 & st3    # set intersection
print(si)   # {1, 5}
print(st1.intersection(st2).intersection(st3))  # {1, 5}
print(st1.intersection(st2, st3))  # {1, 5}

