def is_subseuence(lst_main, lst_check):
    if len(lst_check) == 0:
        return True     # special case

    # Iterate on the main list, for every number
    # if it the FIRST number in lst_check
    # then lst_check so far in order
    # we remove it
    # if all lst_check is empty: we found them: consective and in order
    for item in lst_main:
        if item == lst_check[0]:
            lst_check.pop(0)    # pop(0) is efficient

    return len(lst_check) == 0


if __name__ == '__main__':
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    status = is_subseuence(lst1, lst2)

    if status:
        print('YES')
    else:
        print('NO')

