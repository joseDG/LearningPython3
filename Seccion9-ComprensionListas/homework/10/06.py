
def smallest_pair(lst):
    # calculate Ai+Aj+j-i for every pair (i,j)

    ans = None
    for pos1, item1 in enumerate(lst):
        for pos2 in range(pos1+1, len(lst)):
            item2 = lst[pos2]

            cur = item1 + item2 + pos2 - pos1

            if ans is None or ans > cur:
                ans = cur
    return ans


if __name__ == '__main__':
    lst = list(map(int, input().split()))

    ans = smallest_pair(lst)
    print(ans)
