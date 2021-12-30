
if __name__ == '__main__':
    lst = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    lst.reverse()   # to make it easy to find last occurrence

    for q in queries:
        idx = -1
        if q in lst:
            idx = lst.index(q)   # idx in reversed list
            idx = len(lst) - idx - 1    # flip to get original

        print('Query', q, 'answer', idx)


# Note this is a nested loop code
    # q in lst is a loop internally
    # lst.index is a loop internally
    # Notice also above 2 loops are of same level (this is not 3 nested loops)