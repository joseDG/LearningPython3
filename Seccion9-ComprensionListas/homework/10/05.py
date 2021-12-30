
def uniqe_not_sorted_lst(lst):
    lst_ret = []

    for idx, item in enumerate(lst):
        # In a sorted list: if the previous number != me ==> I am a new one
        if idx == 0 or lst[idx] != lst[idx-1]:
            lst_ret.append(item)

    return lst_ret


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    lst = uniqe_not_sorted_lst(lst)
    print(lst)
