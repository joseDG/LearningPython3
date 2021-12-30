
def digits_frequency(lst):
    freq = [0] * 10     # to compute fromquency from 0 to 9

    for value in lst:
        value = abs(value)  # get rid of the sign

        if value == 0:
            freq[0] += 1    # special case
        else:
            while value > 0:
                digit = value % 10
                value //= 10
                freq[digit] += 1

    return freq


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    freq = digits_frequency(lst)

    for idx in range(10):
        print(idx, freq[idx])

"""
test case for you
78 0 0 0 -307

Output
0 4
1 0
2 0
3 1
4 0
5 0
6 0
7 2
8 1
9 0
"""