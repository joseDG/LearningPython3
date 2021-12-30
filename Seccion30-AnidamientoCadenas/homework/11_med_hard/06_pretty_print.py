def read_matrix_strings():
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = input().split()
    return rows, len(lst_of_lsts[0]), lst_of_lsts

if __name__ == '__main__':
    rows, cols, matrix = read_matrix_strings()

    # for each column, get all words, compute their word length, get max of all
    width_per_col = [max([len(word) for word in col]) for col in zip(*matrix)]

    # for each word in a row, ljust based on its column max width
    # then join all of them by ' # '
    # logic: for every row => transform the row and merge
    matrix = [' # '.join([word.ljust(width_per_col[idx]) for idx, word in enumerate(row)]) for row in matrix]
    print('\n'.join(matrix))    # print rows newline seperated
