
def is_increasing(lst):
    # compare every element to the last one
    for pos in range(1, len(lst)):
        if lst[pos] < lst[pos-1]:
            return False
    return True


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    status = is_increasing(lst)

    if status:
        print('YES')
    else:
        print('NO')


# can we make it more pythonic without explicit loop
