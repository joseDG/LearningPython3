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
    c1, c2 = map(int, input().split())

    for row in matrix:  # observe change in row change original matrix
        row[c1], row[c2] = row[c2], row[c1]

    print(matrix)

