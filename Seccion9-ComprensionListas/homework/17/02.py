def is_subslist(lst_main, lst_check):
    if len(lst_check) == 0:
        return True  # special case

    if len(lst_check) > len(lst_main):
        return False

    # For each index: generate a sublist and check
    for idx in range(len(lst_main) - len(lst_check) + 1):
        if lst_check == lst_main[idx: idx + len(lst_check)]:
            return True

    return False

    # as slice is not memory efficient, this is not the most efficient code
    # Another wat: internal loop to check the list step by step and stop early

    # in practice: if list will be small: you should code it in a nice way
    # if the efficient way is more effort to write by you / read by others
    # code clarity is an important factor in industry
    # not just efficiency that is not really added value
    # I am just training you to be a better problem solver :)


if __name__ == '__main__':
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    status = is_subslist(lst1, lst2)

    if status:
        print('YES')
    else:
        print('NO')

