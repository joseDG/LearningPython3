
def find_3_min(lst):
    mn_lst = []
    # the idea: keep aading to this list
    # sort and remove the 4th item
    # then the list always have the min 3 numbers

    for item in lst:
        mn_lst.append(item)

        if len(mn_lst) > 3:
            mn_lst.sort()
            mn_lst.pop()

    mn_lst.sort()
    return mn_lst



if __name__ == '__main__':
    lst = list(map(int, input().split()))

    mn_lst = find_3_min(lst)
    print(mn_lst)
