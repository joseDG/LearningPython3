
def filter_duplicates_preserve_order(lst_of_lsts):
    # Convert internal  list into tuples to be immutable
    tpls = [tuple(lst) for lst in lst_of_lsts]
    my_dict = list(dict.fromkeys(tpls)) # get rid of duplicates
    return [list(tup) for tup in my_dict]

if __name__ == '__main__':
    print(filter_duplicates_preserve_order([[7, 1], [2, 4],
                                            [7, 1], [5, 2], [2, 4]]))
