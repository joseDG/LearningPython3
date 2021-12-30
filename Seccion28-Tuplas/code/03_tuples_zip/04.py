

# what if sequences are of different length?
# It stops at the shortest length

items = list(zip(range(10, 15), range(100)))
print(items)
# [(10, 0), (11, 1), (12, 2), (13, 3), (14, 4)]
# observe stopped only after 5 elements!

# unzip
seq1, seq2 = zip(*items)
print(seq1)     # (10, 11, 12, 13, 14)
print(seq2)     # (0, 1, 2, 3, 4)

