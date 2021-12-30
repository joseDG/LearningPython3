
def deep_reverse(lst):
    for item in lst:    # reverse every item
        if isinstance(item, list):
            deep_reverse(item)

    lst.reverse()       # reverse list itself


if __name__ == '__main__':


    lst = [1, [2, 3, 4], [5, 6]]
    lst.reverse()   # top level reverse ONLY
    print(lst)  # [[5, 6], [2, 3, 4], 1]

    lst = [1, [2, 3, 4], [5, 6]]
    deep_reverse(lst)   # reverse very deep lists
    print(lst)  # [[6, 5], [4, 3, 2], 1]

    lst = [1, [2, 3, 4], [5, [6, 7, 8]]]
    deep_reverse(lst)
    print(lst)  # [[[8, 7, 6], 5], [4, 3, 2], 1]

    lst = [1, [2, 3, 4], [5, [6, 7, [8, 9.5, 'hey']]]]
    deep_reverse(lst)
    print(lst)  # [[[['hey', 9.5, 8], 7, 6], 5], [4, 3, 2], 1]

