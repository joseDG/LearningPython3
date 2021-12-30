

def our_reverse(lst):
    for pos1 in range(len(lst) // 2):
        pos2 = len(lst) - pos1 - 1  # the opposite in the list
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]


def main():
    lst = list(map(int, input().split()))

    our_reverse(lst)

    print(lst)


main()
