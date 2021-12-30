cnt = 0

for x in range(50, 301):
    start = max(70, x + 1)

    for y in range(start, 401):
        if (x + y) % 7 == 0:
            cnt += 1
print(cnt)
