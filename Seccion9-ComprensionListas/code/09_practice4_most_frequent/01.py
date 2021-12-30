

def most_frequent_slow(lst):
    most_value, frequency = None, 0
    for value in lst:
        cnt = lst.count(value)
        if cnt > frequency:
            most_value, frequency = value, cnt
        elif cnt == frequency:
            most_value = min(most_value, value)
    return most_value, frequency


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    most_value, frequency = most_frequent_slow(lst)
    print('Value', most_value, 'repeated', frequency)


