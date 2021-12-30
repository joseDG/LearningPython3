
# The key to remove properly is to remove from the end to the begin
# if you tried to remove from the begin the list will be corrupted

def remove_evens_inplace1(lst):
    # iterate backward
    for pos in range(len(lst)-1, -1, -1):
        if lst[pos] % 2 == 0:
            del lst[pos]
    return lst


def remove_evens_inplace2(lst):
    # iterate on revered but get the right index
    sz = len(lst)   # important. take it here as list will be updated
    for pos, item in enumerate(reversed(lst)):
        if item % 2 == 0:
            pos = sz - pos - 1    # idx in original list
            # recall pos will be reassigned in every iteration
            del lst[pos]
    return lst



if __name__ == '__main__':
    lst = list(map(int, input().split()))

    remove_evens_inplace2(lst)

    print(lst)


