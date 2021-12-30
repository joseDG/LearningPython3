

def print_lst_of_lsts(lst_of_lsts):
    for lst in lst_of_lsts:
        print(lst)

def read_lst_of_lsts_ints():
    rows = int(input())
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return lst_of_lsts

lsts = read_lst_of_lsts_ints()
print_lst_of_lsts(lsts)

"""
3
1 2 3 4 
5 6 
7 8 9 10 11 

[1, 2, 3, 4]
[5, 6]
[7, 8, 9, 10, 11]
"""