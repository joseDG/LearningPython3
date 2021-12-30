

def deep_reverse(lst):
    return list(reversed([item if not isinstance(item, list) else deep_reverse(item) for item in lst]))


if __name__ == '__main__':
    lst = [1, [2, 3, 4], [5, 6]]
    print(deep_reverse(lst))    # [[6, 5], [4, 3, 2], 1]

    lst = [1, [2, 3, 4], [5, [6, 7, 8]]]
    print(deep_reverse(lst))    # [[[8, 7, 6], 5], [4, 3, 2], 1]

    lst = [1, [2, 3, 4], [5, [6, 7, [8, 9.5, 'hey']]]]
    print(deep_reverse(lst))    # [[[['hey', 9.5, 8], 7, 6], 5], [4, 3, 2], 1]