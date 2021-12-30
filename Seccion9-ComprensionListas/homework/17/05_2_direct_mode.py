"""
We want to handle when k is so big

Let's say remaining_alive = 4 and k = 6
This is the same as if k = 2   (6%4 = 2)

Similarly
Let's say remaining_alive = 4 and k = 10
This is the same as if k = 2   (10%4 = 2)

This is the same as the useless cycles in the clock
    e.g. 4 is same as any 4 + k*12

So in general, we don't need to iterate k times
we only need: k % remaining_alive
"""

def josephus(n, k):
    lst = [idx + 1 for idx in range(n)] # assign 1 2 3 4 5 ... n

    # Note creating length at once is MORE efficient than N appends

    last_pos = 0
    ret = [0] * n   # let's avoid a lot of appends (if efficiency matters)

    for pos in range(n-1):  # the range will be created once with the original n
        #for step in range(k-1):
        #    last_pos = (last_pos + 1) % n   # % can join these lines!
        last_pos = (last_pos + k - 1) % n

        ret[pos] = lst[last_pos]
        lst.pop(last_pos)
        n = len(lst)  # list is shrinking
        last_pos %= n

    ret[-1] = lst[0]

    return ret




if __name__ == '__main__':
    n, m = map(int, input().split())

    print(josephus(n, m))

