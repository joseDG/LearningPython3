
# 7 students x 4 subjects
grades = [  [50, 33, 40, 30],
            [35, 50, 44, 17],
            [30, 35, 50, 37],
            [50, 35, 44, 22],
            [50, 44, 50, 30],
            [50, 36, 18, 50],
            [35, 30, 47, 16]]

def compute_row_avg(lst_of_lsts):
    row_avg = []

    for lst in lst_of_lsts:
        sum = 0
        for item in lst:
            sum += item
        row_avg.append(sum / len(lst))
    return row_avg

print(compute_row_avg(grades))
# [38.25, 36.5, 38.0, 37.75, 43.5, 38.5, 32.0]

# can we pythonic it?
