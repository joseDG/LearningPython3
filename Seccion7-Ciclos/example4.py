n, a, b = [*map(int, input().split())]

total = 0

for i in range(1, n + 1):
    tmp = i
    digits_sum = 0

    while tmp > 0:
        digits_sum += tmp % 10
        tmp //= 10

    if a <= digits_sum <= b:
        total += i

print(total)
