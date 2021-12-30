

def print1(lst_of_lsts):
    for lst in lst_of_lsts:
        print(*lst) # unpack: print without []


grades = [  [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9, 10, 11],
        ]

print1(grades)
"""
1 2 3 4
5 6
7 8 9 10 11
"""