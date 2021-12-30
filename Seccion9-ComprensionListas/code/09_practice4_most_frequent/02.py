
def most_frequent_fast(lst):
    # it actually work well. max here is flexible
    freq_lst  = [0] * (max(lst)+1)

    for value in lst:
        freq_lst[value] += 1

    # argmax - Observe: the tie is also handled!
    most_value = freq_lst.index(max(freq_lst))

    return most_value, freq_lst[most_value]


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    most_value, frequency = most_frequent_fast(lst)
    print('Value', most_value, 'repeated', frequency)


