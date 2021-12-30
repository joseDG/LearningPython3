



if __name__ == '__main__':


    lst = list(map(int, input().split()))
    dict = {}
    for value in lst:
        dict.setdefault(value, 0)
        dict[value] += 1

    mx = max(dict.values())
    freq = sorted([key for key, value in dict.items() if value == mx])
    print(f'The highest frequency is {mx} for values: {freq}')
