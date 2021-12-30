


def left_max(lst):
    if len(lst) <= 1:   # handling 2 base case with single condition
        return lst

    # at least 2 elements
    head = left_max(lst[:-1])
    last = max(head[-1], lst[-1])
    head.append(last)
    return head




if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2]

    print(left_max(lst))  # [1, 3, 5, 7, 7, 7]