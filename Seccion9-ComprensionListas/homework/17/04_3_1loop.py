# caution: this is hard. Try and comeback later

# 1 loop
# Even the last idea has duplicate of computations
# If we know our best increasing lst is [1, 2, 3, 4]
# why trying from 2 to reach 4, then from 3 to reach?
# We already know we have 4*5/2 valid sequences (all start and end)

# idea
# Get your max increasing sequence. Now this adds n*(n+1)/2
    # for simplicity, just add the current sequence length
# Move to the next start. And so on


def count_increasing(lst):
    total = len(lst)    # initally for sequence of length 1
    cur_len = 1

    for idx in range(1, len(lst)):
        # Keep expand the current valid sequence if possible
        if lst[idx-1] <= lst[idx]:
            total += cur_len    # At each step: we have cur_len ending at this position
            cur_len += 1    # add another element
        else:
            cur_len = 1     # start a new sequence

    return total

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(count_increasing(lst))

