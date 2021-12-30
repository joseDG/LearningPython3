


def list_accumulate(lst):
    if len(lst) <= 1:   # handling 2 base case with single condition
        return lst

    # at least 2 elements
    head = list_accumulate(lst[:-1])
    last = head[-1] + lst[-1]
    head.append(last)
    return head




if __name__ == '__main__':
    lst = [1, 8, 2, 10, 3]

    print(list_accumulate(lst))  # [1, 9, 11, 21, 24]