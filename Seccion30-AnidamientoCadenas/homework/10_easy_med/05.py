def read_matrix():
    # read and return: rows, cols, list of lists
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()

    # for each case list the needed indices
    # use list comprehension to extract the target position

    last_row = sum(matrix[-1])
    last_col = sum([row[-1] for row in matrix])
    left_diag = sum([row[idx] for idx, row in enumerate(matrix)])
    # -(idx+1) ==> -1, -2, -3, etc till #rows
    right_diag = sum([row[-(idx + 1)] for idx, row in enumerate(matrix)])

    print(last_row, last_col)
    print(left_diag, right_diag)