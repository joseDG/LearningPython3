
lst = ['mostafa', 'saad', 'ibrahim']
print(lst[2])       # ibrahim
print(lst[2][1])    # b

lst2 = [lst, (5, 7, 2)]
print(lst2[0][2][1])    # b
print(lst2[1][1])       # 7

lst.sort()
print(lst)
# ['ibrahim', 'mostafa', 'saad']


lst = [[[[1]]]]
print(lst)                  # [[[[1]]]]
print(lst[0])               # [[[1]]]
print(lst[0][0])            # [[1]]
print(lst[0][0][0])         # [1]
print(lst[0][0][0][0])      # 1

