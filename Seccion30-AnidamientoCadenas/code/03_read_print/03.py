
def print2(lst_of_lsts):
    for i, lst in enumerate(lst_of_lsts):
        for j, item in enumerate(lst):
            print(item, end=' ')
        print()

def print3(lst_of_lsts):    # for educational purposes
    for i in range(len(lst_of_lsts)):
        for j in range(len(lst_of_lsts[i])):
            print(lst_of_lsts[i][j], end=' ')
        print()


grades = [  [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9, 10, 11],
        ]

print2(grades)
"""
1 2 3 4 
5 6 
7 8 9 10 11 
"""