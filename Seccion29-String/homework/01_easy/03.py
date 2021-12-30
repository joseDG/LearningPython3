

if __name__ == '__main__':
    line = input() + '$'    # to make coding easier: add char that is not part of input

    res = []
    group_start_idx = 0
    for idx in range(1, len(line)):
        # as long as same char, let's keep expanding - .lower to avoid casing
        if line[idx].lower() != line[idx-1].lower():
            res.append(line[group_start_idx : idx])    # cut a group
            group_start_idx = idx # next group start

    print(','.join(res))
    # an iterative way for the comma - just for educational purpose
    #for idx, item in enumerate(res):
    #    sep = ',' if idx != len(res)-1 else ''  # always , except the last entry empty
    #    print(item, end=sep)

