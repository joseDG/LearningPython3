"""
Assume a list: 1 0 3 -4 2  -6 9
Sliding window (sublist): 3
Let’s print all windows of length 3 and their sum
1 0 3       ⇒ sum = 4
  0 3 -4      ⇒ sum = -1                 [observe 0 3 are common]
    3 -4 2      ⇒ sum = 1
      -4 2 -6     ⇒ sum = -8
         2 -6 9      ⇒ sum = 5

So we can build the first window: 1 0 3
    Then keep add and remove an item

    O(N)

If you found this is hard for you, come back later
"""


def maxium_sum_fixed_window(lst, k):
    assert k <= len(lst)

    window = sum(lst[:k])  # first k elements
    start_idx, max_sum = 0, window

    # idx here is actually the last element in the list
    for idx in range(k, len(lst)):
        window = window - lst[idx - k] + lst[idx]  # - lst[idx-k] remove the first of last window.

        if max_sum < window:
            max_sum, start_idx = window, idx - (k - 1)

    return start_idx, max_sum


# Nest loop sol: O(N)


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    k = int(input())

    start_idx, max_sum = maxium_sum_fixed_window(lst, k)

    print(start_idx, max_sum)

