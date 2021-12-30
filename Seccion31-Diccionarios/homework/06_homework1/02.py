"""
For every type, maintain a list in a dict
Order the values of every type
Flatten the lists

From python 3.7, the order is preserved. Hence the lists already sorted by type :)
"""

def sort_different_types(lst):

    dict = {}
    for item in lst:
        t = type(item)
        dict.setdefault(t, [])
        dict[t].append(item)

    #SyntaxError: iterable unpacking cannot be used in comprehension
    #return [*sorted(lst) for lst in dict.values()]
    lsts = [sorted(lst) for lst in dict.values()]
    return [item for lst in lsts for item in lst]



if __name__ == '__main__':
    lst = [10, 'most', 2.5, 7, 'aly', 9, 4.5, 2, 'ziad', -4, 1.1, [1, 5], 5, [0, 7, 8]]
    print(sort_different_types(lst))

