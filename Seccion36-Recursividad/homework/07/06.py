


def list_increment(lst):
    if len(lst) == 0:
        return []

    cur = lst[0] + len(lst)
    return [cur] + list_increment(lst[1:])




if __name__ == '__main__':
    lst = [1, 8, 2, 10, 3]

    print(list_increment(lst))  # [6, 12, 5, 12, 4]