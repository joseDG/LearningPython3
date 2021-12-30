# 3 nested loops
# slow but simple to read

def is_increasing(lst):
    # compare every element to the last one
    for pos in range(1, len(lst)):
        if lst[pos] < lst[pos-1]:
            return False
    return True


def count_increasing(lst):
    total = 0
    for idx1 in range(len(lst)):
        for idx2 in range(idx1, len(lst)):
            total += is_increasing(lst[idx1 : idx2 + 1])
    return total

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(count_increasing(lst))

