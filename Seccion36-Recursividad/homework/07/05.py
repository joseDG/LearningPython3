


def list_avg(lst):
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    n = len(lst)
    # This sublist is average of n-1 elements. Let's get the sum
    sub = list_avg(lst[1:]) * (n-1)

    return (lst[0] + sub) / n



if __name__ == '__main__':
    print(list_avg([5]))           # 5
    print(list_avg([5, 7]))        # 6.0
    print(list_avg([1, 2, 3, 4]))  # 2.5