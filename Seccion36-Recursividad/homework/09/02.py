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

def get_path_sum(matrix, r = 0, c = 0): # from the old homework
    total_sum = matrix[r][c]
    rows, cols = len(matrix), len(matrix[0])

    if not (positions := get_neibghours(r, c, rows, cols)):
        return total_sum

    values = [matrix[i][j] for i, j in positions]
    r, c = positions[argmax(values)]

    total_sum += get_path_sum(matrix, r, c)

    return total_sum


if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    print(get_path_sum(matrix))
