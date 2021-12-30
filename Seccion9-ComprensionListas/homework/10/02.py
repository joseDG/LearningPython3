
def replace_min_max_inplace(lst):
    mn = min(lst)
    mx = max(lst)

    for idx, item in enumerate(lst):
        if item == mn:
            lst[idx] = mx
        elif item == mx:
            lst[idx] = mn


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    replace_min_max_inplace(lst)
    print(lst)
