a, b, c = [*map(int, input().split())]

if a >= 100 and b >= 100 and c >= 100:
    res = -1
else:
    if a < 100:
        res = a
    elif b < 100:
        res = b
    else:
        res = c

    if res < a < 100:
        res = a

    if res < b < 100:
        res = b

    if res < c < 100:
        res = c

print(res)
