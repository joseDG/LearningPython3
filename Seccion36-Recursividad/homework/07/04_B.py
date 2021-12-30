


def list_max(lst):
    first, *lst = lst

    if not lst:
        return first

    if first > (sub := list_max(lst)):
        return first

    return sub


if __name__ == '__main__':
    print(list_max([5]))                            # 5
    print(list_max([5, 7]))                         # 7
    print(list_max(['most', 'saad', 'ibrahim']))    # saad