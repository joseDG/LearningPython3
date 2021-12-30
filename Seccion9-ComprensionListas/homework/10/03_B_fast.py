
if __name__ == '__main__':
    lst = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    # As values are 0-500, we can make list of 501 mark the last value in it
    # Then we answer the queries directly

    last_value_pos = [-1] * 501     # 501 values that are -1 (default for not exist)

    # mark in the list where the item appear
    # as we process in order: the last occurrence overwrite previous values
    for idx, item in enumerate(lst):
        last_value_pos[item] = idx

    for q in queries:
        assert q < len(last_value_pos)
        print('Query', q, 'answer', last_value_pos[q])

# Linear time solution! O(N)
