
def filter_duplicates(lst_of_lsts):
    st = set()
    result = []

    for lst in lst_of_lsts:
        tup = tuple(lst)    # must use immutable objects
        if tup not in st:
            st.add(tup)
            result.append(lst)
    return result

if __name__ == '__main__':
    print(filter_duplicates([[7, 1], [2, 4],
                             [7, 1], [5, 2], [2, 4]]))
