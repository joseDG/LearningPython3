# 3 nested loops
# slow but simple to read

def longest_subarray(lst):
    best_len = None

    # try all windows
    for idx1 in range(len(lst)):
        for idx2 in range(idx1+1, len(lst)):
            # for every window count zeros and ones then compare
            # we can add extra check or handling to avoid odd-length lists
            sub_list = lst[idx1 : idx2 + 1]
            zeros_len = sub_list.count(0)
            ones_len = len(sub_list) - zeros_len
            if zeros_len == ones_len:
                if best_len is None or best_len < len(sub_list):
                    best_len = len(sub_list)

    return best_len

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(longest_subarray(lst))

