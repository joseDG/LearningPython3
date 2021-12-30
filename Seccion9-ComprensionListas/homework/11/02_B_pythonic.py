# More pythonic - Readable code
# Less prone to error
# Shorter!

def digits_frequency(lst):
    freq = [0] * 10

    for value in lst:
        # Convert the number to a string and add it
        string = str(abs(value))
        for char in string:
            freq[int(char)] += 1

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