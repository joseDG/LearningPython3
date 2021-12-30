
# 7 students x 4 subjects
grades = [  [50, 33, 40, 30],
            [35, 50, 44, 17],
            [30, 35, 50, 37],
            [50, 35, 44, 22],
            [50, 44, 50, 30],
            [50, 36, 18, 50],
            [35, 30, 47, 16]]

# assume equal columns / at least 1 seq
def compute_col_avg(lst_of_lsts):
    # let's iterate column-major order
    col_avg = []

    for j in range(len(lst_of_lsts[0])):
        sum = 0
        for i in range(len(lst_of_lsts)):
            sum += lst_of_lsts[i][j]
        col_avg.append(sum / len(lst_of_lsts))
    return col_avg

print(compute_col_avg(grades))
#[42.85, 37.5, 41.85, 28.85]

# can we pythonic it?
