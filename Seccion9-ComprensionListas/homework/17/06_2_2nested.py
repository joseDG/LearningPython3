# 2 nested loops

def longest_subarray(lst):
    best_len = None

    # Try all windows starting from each index
    for idx1 in range(len(lst)):
        # keep expanding the list from idx1 updating zeros and ones count
        ones_count, zeros_count = 0, 0
        for idx2 in range(idx1, len(lst)):

            if lst[idx2] == 0:
                zeros_count += 1
            else:
                ones_count += 1

            if zeros_count == ones_count:
                cur_len = idx2 - idx1 + 1

                if best_len is None or best_len < cur_len:
                    best_len = cur_len

    return best_len

if __name__ == '__main__':
    lst = list(map(int, input().split()))

    print(longest_subarray(lst))

