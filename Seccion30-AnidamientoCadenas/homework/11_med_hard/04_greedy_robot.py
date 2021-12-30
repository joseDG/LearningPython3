def read_matrix():
    # read and return: rows, cols, list of lists
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts


def is_within_grid(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols


def get_neibghours(i, j, rows, cols):
    dir = [(1, 0), (0, 1), (1, 1)]
    return [(r, c) for di, dj in dir
            if is_within_grid(r := i + di, c:= j + dj, rows, cols)]


def argmax(lst):
    return lst.index(max(lst))


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    r, c, total_sum = 0, 0, 0

    while True:
        total_sum += matrix[r][c]
        if not (positions := get_neibghours(r, c, rows, cols)):
            break   # get the list: if empty, break
        values = [matrix[i][j] for i, j in positions]
        r, c = positions[argmax(values)]

    print(total_sum)
