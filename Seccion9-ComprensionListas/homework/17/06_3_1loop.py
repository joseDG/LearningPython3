# HARD
# 1 loop

"""
Assume input

index 0 1 2 3 4
value 1 1 1 0 0

How many ones and zeros at position 0: (1, 0)
How many ones and zeros at position 4: (3, 2)   => cancel 1s with 0s ==> (1, 0)

What does it mean to have 2 positions with same value of: total ones - total zeros?
    It means the values in between the 2 positions must have ones = zeros
        Specifically from pos 1 to pos 4


Algorithm:
- Keep accumulating current value to compute total ones - total zeros
- use 2 arrays one for postivie value and one for -ve  (or use one list with a shifted value)
- If first time to see such value: mark it
- if you met it before: we have a new valid range


"""


def longest_subarray(lst):
    best_len = None

    postives = [-1] * (len(lst) + 1)
    negatives = [-1] * (len(lst) + 1)

    accumulation = 0

    for idx, item in enumerate(lst):
        first_idx = None

        if item == 0:
            accumulation -= 1
        else:
            accumulation += 1

        if accumulation == 0:
            best_len = idx + 1
        elif accumulation > 0:
            if postives[accumulation] == -1:  # such accumulation never appeared
                postives[accumulation] = idx  # mark the first idx for that
            else:
                first_idx = postives[accumulation]
        else:
            if negatives[-accumulation] == -1:
                negatives[-accumulation] = idx
            else:
                first_idx = negatives[-accumulation]

        if first_idx is not None:
            cur_len = idx - first_idx

            if best_len is None or best_len < cur_len:
                best_len = cur_len

    return best_len if best_len is not None else 0

# later with dict: the code can be simplified

# By replacing 0 as -1, each group of equal ones and zeros is actually sublist of zero sum

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(longest_subarray(lst))

