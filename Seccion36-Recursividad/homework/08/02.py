


def list_accumulate(lst, ln = None):
    if ln is None:
        ln = len(lst)

    if ln <= 1:
        return

    list_accumulate(lst, ln - 1)    # accumulate first N-1 elements
    # Last element of N-1 has all accumulation of first N-1 elements (lst[ln - 2])
    lst[ln - 1] += lst[ln - 2]





if __name__ == '__main__':
    lst = [1, 8, 2, 10, 3]
    list_accumulate(lst)

    print(lst)  # [1, 9, 11, 21, 24]