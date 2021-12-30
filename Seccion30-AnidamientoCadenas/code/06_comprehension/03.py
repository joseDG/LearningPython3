
# we know with zip we can create iterator over item from each
# what if we want all pairs

lst1 = [1, 2]
lst2 = [10, 20, 30]

# without comprehension
lst_pairs1 = []
for item1 in lst1:
    for item2 in lst2:
        lst_pairs1.append((item1, item2))
print(lst_pairs1)   # [(1, 10), (1, 20), (1, 30_oop), (2, 10), (2, 20), (2, 30_oop)]


lst_pairs2 = [(item1, item2) for item1 in lst1 for item2 in lst2 ]
