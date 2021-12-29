x, a1, a2, a3, a4, a5 = [*map(int, input().split())]
cnt = 0

cnt += a1 <= x
cnt += a2 <= x
cnt += a3 <= x
cnt += a4 <= x
cnt += a5 <= x

print(cnt, 5 - cnt)
