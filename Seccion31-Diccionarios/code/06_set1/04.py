

st1 = {1, 3, 5, 7, 8, 10}

st1.add(-20)
st1.remove(10)
#st1.remove(30_oop)  # if not exist, error => KeyError
st1.discard(30)  # if not exist, no problem
print(st1)  # {1, 3, 5, 7, 8, -20}

print(st1.pop())    # remove random element. If empty = error
st1.clear() # remove elements