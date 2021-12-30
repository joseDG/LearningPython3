def read_matrix():
    # read and return: rows, cols, list of lists
    rows = int(input())
    assert rows > 0
    lst_of_lsts = [0] * rows

    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input().split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts

def argmax_first(lst):  # first occurance of max
    return lst.index(max(lst))

def argmax_last(lst):   # last occurance of max
    return len(lst) - lst[::-1].index(max(lst)) -1

def flat_matrix(matrix):
    return [value for row in matrix for value in row]

def from1d_to_2d(cols, idx):
    return idx//cols, idx % cols

if __name__ == '__main__':
    # Another way: inefficient but educational
    rows, cols, matrix = read_matrix()
    lst = flat_matrix(matrix)
    idx = argmax_last(lst)
    pos = from1d_to_2d(cols, idx)

    print(f'Max value at position {pos} with value = {lst[idx]}')
