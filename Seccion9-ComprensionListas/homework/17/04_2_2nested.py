# 2 nested loops
# simple observation to remove a loop
    # we are duplicating effort
# let's say from idx1=5 to idx2=7
    # we have list 3 5 7 which is increasing
    # now if next element is 9, we know this is one more valid sequence

# algorithm: from every start: keep going as long as it is valid one
    # for every possible element to keep it increasing, add one


def count_increasing(lst):
    total = 0

    # for every index idx1 in the array we consider it as the start of a sublist
    for idx1 in range(len(lst)):
        total += 1  # lst of len 1

        for idx2 in range(idx1+1, len(lst)):
            if lst[idx2] >= lst[idx2-1]: # is still increasing with a new element? Add 1
                total += 1
            else:
                break   # not increasing any more. Try a new start by idx1

    return total

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(count_increasing(lst))

