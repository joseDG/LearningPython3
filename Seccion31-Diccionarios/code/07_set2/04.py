
st1 = {1, 5, 7, 8}
st2 = {1, 5, 3, 10}

st1 |= st2  # union and update st1
st2.update(st1)

# same &= ^=
