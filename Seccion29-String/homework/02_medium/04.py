

def our_replace(main_str, pattern, repalce_with):
    idx = 0
    res = ''
    n = len(pattern)

    if n == 0:
        return main_str


    while idx < len(main_str):
        # If matched: add and jump. Otherwise move to the next step
        substr = main_str[idx:idx + n]
        if substr == pattern:
            res += repalce_with
            idx += n
        else:
            res += main_str[idx]
            idx += 1
    return res
    # the code can be improved. For example: all these += are inefficient


if __name__ == '__main__':
    main_str, pattern, repalce_with = input().split()

    print(our_replace(main_str, pattern, repalce_with))


