
# Direct Simulation!

def josephus(n, k):
    lst = [0] * n

    for idx in range(n):
        lst[idx] = idx + 1  # assign 1 2 3 4 5 ... n

    # Note creating length at once is MORE efficient than N appends

    last_pos = 0
    ret = []

    while len(lst) > 1:
        # first guy is counted. Iterate k-1 steps
        for step in range(k-1):
            last_pos += 1
            if last_pos == n:   # let's cycle
                last_pos = 0    # go back to begin

        ret.append(lst[last_pos])
        lst.pop(last_pos)
        n = len(lst)  # list is shrinking
        if last_pos == n:
            last_pos = 0

    ret.append(lst[0])

    return ret




if __name__ == '__main__':
    n, m = map(int, input().split())

    print(josephus(n, m))

