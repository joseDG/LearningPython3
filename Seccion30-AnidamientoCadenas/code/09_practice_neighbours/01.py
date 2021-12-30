

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

def get_neibghours(i, j, rows, cols, cnt = 8):
    # {d, r, u, l, ul, dr, ur, dl};
    di = [1, 0, -1, 0, -1, 1, -1, 1]
    dj = [0, 1, 0, -1, -1, 1, 1, -1]

    # Filter the positions that are outside the grid
    #return [(i+di[d], j+dj[d]) for d in range(cnt)
        # if is_within_grid(i+di[d], j+dj[d], rows, cols)]
    return [(r, c) for d in range(cnt)
                if is_within_grid(r := i + di[d], c:= j + dj[d], rows, cols)]

if __name__ == '__main__':
    rows, cols, matrix = read_matrix()

    if rows == cols == 1:
        print(0, 0)
        exit(0)

    for r in range(rows):
        for c in range(cols):
            positions = get_neibghours(r, c, rows, cols)
            mx = max([matrix[i][j] for i, j in positions])
            if matrix[r][c] > mx:
                print(r, c)

# test a matrix with single value or single row
