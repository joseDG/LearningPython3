
def uniqe_not_sorted_lst(lst):
    lst_ret = []

    for item in lst:
        if item not in lst_ret:
            lst_ret.append(item)

    return lst_ret


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    lst = uniqe_not_sorted_lst(lst)
    print(lst)
