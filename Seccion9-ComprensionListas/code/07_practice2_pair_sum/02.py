

def pair_maxsum_slow(lst):
    pos1, pos2 = 0, 1

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
                pos1, pos2 = i, j

    return pos1, pos2

def main():
    lst = list(map(int, input().split()))
    assert len(lst) > 1

    pos1, pos2 = pair_maxsum_slow(lst)

    print('idx1', pos1, 'value', lst[pos1])
    print('idx2', pos2, 'value', lst[pos2])
    print('Max sum', lst[pos1] + lst[pos2])

main()