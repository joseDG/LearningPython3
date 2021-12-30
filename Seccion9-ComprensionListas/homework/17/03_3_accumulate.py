"""
Caution: this is hard. Skip if so


Let's say we have the list 1 2 3 4
An accumulated list: each element is sum of all previous elements
E.g. 1 3 6 10           (observe 6=1+2+3, 10 = 1+2+3+4)

Now to build this accumulation we can do nested loops, but what is the benfit

With a simple observation: we can make the accumulation in a single loop!

Observe: 10 = 4 + 6 which is the previous sum
    In other words: My sum = My element + My neighbour Sum. See the first loop: lst[idx] += lst[idx-1]

Now we built the accumulation: how to make use of it?
We know lst[idx] is the sum of all elements from 0 to index
But we need the sum of a window idx1 to idx2
This is simply: lst[idx2] - lst[idx1 - 1]

E.g. if idx1 = 2 and idx2 = 3      (which should be [3, 4])
lst[3]   = 1 + 2 + 3 + 4
lst[2-1] = 1 + 2
Subtraction is 3 + 4

The advantage of this approach: we can compute any range in sum in a single step (we call it O(1))

So hard? skip :)



"""


def maxium_sum_fixed_window(lst, k):
    assert k <= len(lst)

    # Compute accumulate sum: A[i] = Sum of all previous elements
    for idx in range(1, len(lst)):
        lst[idx] += lst[idx - 1]

    start_idx, max_sum = 0, lst[k - 1]

    # idx here is actually the last element in the list
    for idx in range(k, len(lst)):
        window = lst[idx] - lst[idx - k]

        if max_sum < window:
            max_sum, start_idx = window, idx - (k - 1)

    return start_idx, max_sum


# Nest loop sol: O(N)


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    k = int(input())

    start_idx, max_sum = maxium_sum_fixed_window(lst, k)

    print(start_idx, max_sum)

