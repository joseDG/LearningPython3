s1, e1, s2, e2 = [*map(int, input().split())]

if e1 < s2 or e2 < s1:
    print(-1)
else:
    if s1 < s2:
        s1 = s2
    if e1 > e2:
        e1 = e2

    print(s1, e1)
