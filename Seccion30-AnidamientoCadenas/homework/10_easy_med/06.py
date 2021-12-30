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
    target_val = int(input())

    for idx, col in enumerate(zip(*matrix)):
        if target_val in col:
            print(f'found in col {idx}')
            break
    else:
        print('Not found')

