# Recall

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9, 10, 11, 12, 13]

print(lst1)      # [1, 2, 3]
print(*lst1)     # 1 2 3   unpack first, then print

conc = [*lst1, *lst2]   # [1, 2, 3, 4, 5, 6] conc lists

l1, l2, l3 = zip(*zip(lst1, lst2, lst3))
print(l1, l2, l3)   # (1, 2, 3) (4, 5, 6) (7, 8, 9)
# transpose(tranpose(matrix)) = matrix


