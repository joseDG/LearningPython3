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

    mx, mx_r, mx_c = None, None, None

    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            if mx is None or mx <= value:       # <= for last occurrence. < for first occurrence
                mx, mx_r, mx_c = value, row_idx, col_idx

    print(f'Max value at position {mx_r, mx_c} with value = {mx}')
