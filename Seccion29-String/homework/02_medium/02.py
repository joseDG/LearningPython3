

# if u have numbers [1, 5, 6]
# if we wanna order small to large: we can use .sort
# large to small: sort(reverse=true)
# here is a nice math trick
# if u multiplied all numbers we -1, then we can use .sort to order them also from large to small

# below i multiply length with -1
# then we can order from small to large both letter and frequency


if __name__ == '__main__':
    line = input() + '$'

    res = []
    group_start_idx = 0
    for idx in range(1, len(line)):
        if line[idx] != line[idx-1]:
            ln = idx - group_start_idx
            res.append( (-ln, line[idx-1]) )
            group_start_idx = idx

    res.sort()
    for idx, (freq, char) in enumerate(res):
        freq = -freq
        if freq == 1:
            res[idx] = char
        else:
            res[idx] = '{}{}'.format(freq, char)

    print('_'.join(res))

