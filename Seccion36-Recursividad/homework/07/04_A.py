


def list_max(lst):
    if len(lst) == 1:
        return lst[0]

    sub = list_max(lst[1:])

    if lst[0] > sub:
        return lst[0]

    return sub


if __name__ == '__main__':
    print(list_max([5]))                            # 5
    print(list_max([5, 7]))                         # 7
    print(list_max(['most', 'saad', 'ibrahim']))    # saad