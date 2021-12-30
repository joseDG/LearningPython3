
# set: unordered
# (don't preserve insertion order / no values order)
# unique: duplicates are ignored
# items: must be immutable

st = set()
st.add(20)
st.add(10)
st.add(20)
st.add(-2537)
st.add(10)
print(st)   # {10, 20, -2537}
