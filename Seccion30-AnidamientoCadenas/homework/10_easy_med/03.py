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

    matrix = [row for row in matrix if row]
    # if row is same as if len(row) > 0
    print(matrix)