
lst = [7, 8, 9, 'Hi']

for pos in range(len(lst)): # C++/Java style
    print(lst[len(lst) - pos - 1], end=' ')
print()

# Python: range(start, end, step)
for idx in range(len(lst) - 1, -1, -1):
    print(lst[idx], end=' ')
print()

# Better
for item in reversed(lst):  # NO copy is created
    print(item, end=' ')
print()

for pos, item in reversed(list(enumerate(lst))):
    print(pos, item, end=' - ')
    # 3 Hi - 2 9 - 1 8 - 0 7

    # be careful:
    # list(iterable) => makes copy: more memory / slower
