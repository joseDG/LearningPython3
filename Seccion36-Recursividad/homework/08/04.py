


def right_max(lst):
    if len(lst) <= 1:   # handling 2 base case with single condition
        return lst

    # at least 2 elements
    head = right_max(lst[1:])
    last = max(head[0], lst[0])
    head.insert(0, last)
    return head




if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2]

    print(right_max(lst))  # [7, 7, 7, 7, 4, 2]