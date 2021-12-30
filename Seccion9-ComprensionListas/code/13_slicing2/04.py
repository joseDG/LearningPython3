

lst = [1, 2, 3, 4, 5, 6, 7]
lst[2] = 100    # 1 2 100 4 5 6 7

lst[3:6] = [982]    # 1 2 100 982 7

lst[1:3] = [10, 11, 12, 13]    # 1 10 11 12 13 982 7

# you need to replace 3 times with LIST OF THREE
#lst[1:6:2] = [1]   # ValueError
lst[1:6:2] = [-1, -2, -3]    # 1 -1 11 -2 13 -3 7
#lst[6:2:-2] = [0]   # ValueError

lst[3:] = [123]     # 1 -1 11 123

lst = [1, 2, 3, 4, 5, 6, 7]

del lst[1:3]            # 1 4 5 6 7

del lst[1:5:2]        # 1 5 7

