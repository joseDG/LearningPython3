def maxium_sum_fixed_window(lst, k):
    start_idx, max_sum = None, None
    # For each index: generate a sublist and check
    for idx in range(len(lst) - k + 1):
        sublist_sum = sum(lst[idx : idx + k])

        if max_sum is None or max_sum < sublist_sum:
            max_sum, start_idx = sublist_sum, idx

    return start_idx, max_sum

# Nest loop sol: O(N^2)
# Observe: the slice needs to iterate O(N) steps.
# The sum needs to iterate O(N)

if __name__ == '__main__':
    lst = list(map(int, input().split()))
    k = int(input())

    start_idx, max_sum = maxium_sum_fixed_window(lst, k)

    print(start_idx, max_sum)

