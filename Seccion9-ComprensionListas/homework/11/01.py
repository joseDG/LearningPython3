
def most_frequent_fast(lst):
    # With simple change we can use the practice code
    # we will shift all the data to start from ZERO (so we can index normally)
    # then later undo the effect
    # to do that: just subtract the minimum
    # e.g. if input is -10 20 -2 9 20
    # the min is -10
    # subtract it from all: 0 30_oop 8 19 30_oop
    # Find max 30_oop. Undo with -10 ==> 20
    mn, mx = min(lst), max(lst)
    freq_lst  = [0] * (mx - mn +1)

    for value in lst:
        print(value - mn)
        freq_lst[value - mn] += 1

    # argmax - Observe: the tie is also handled!
    most_value = freq_lst.index(max(freq_lst))

    return most_value + mn, freq_lst[most_value]


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    most_value, frequency = most_frequent_fast(lst)
    print('Value', most_value, 'repeated', frequency)


