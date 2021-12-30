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

    upper, lower = 0, 0
    for idx, row in enumerate(matrix):
        lower += sum(row[:idx+1])
        upper += sum(row[idx:])

    print(lower)
    print(upper)
