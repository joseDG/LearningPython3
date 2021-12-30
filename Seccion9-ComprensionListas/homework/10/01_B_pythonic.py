def is_increasing(lst):
    # let's make it more pythonic
    # we create a list that allows us to compare element by element

    last_item = lst[len(lst) - 1]
    shifted_lst = lst.copy()
    shifted_lst.pop(0)  # we don't compare first with previous
    shifted_lst.append(last_item)

    # for input      [10 20 30_oop 40]
    # shifted_lst is [20 30_oop 40 40]

    print(lst)
    print(shifted_lst)

    return lst <= shifted_lst


def is_increasing_v2(lst):
    # More pythonic: understand in the future

    return all(x<y for x, y in zip(lst, lst[1:]))



if __name__ == '__main__':
    lst = list(map(int, input().split()))

    status = is_increasing(lst)

    if status:
        print('YES')
    else:
        print('NO')
