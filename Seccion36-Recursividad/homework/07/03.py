


def list_sum(lst):
    if len(lst) == 0:
        return 0

    sub = list_sum(lst[1:])     # 1 2 3 4 5 6

    return lst[0] + sub


if __name__ == '__main__':
    print(list_sum([]))           # 0
    print(list_sum([5]))          # 5
    print(list_sum([5, 7]))       # 12