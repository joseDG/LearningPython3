

def length_3n_plus_1(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + length_3n_plus_1(n // 2)
    else:
        return 1 + length_3n_plus_1(3 * n + 1)


print(length_3n_plus_1(6))  # 9 for sequence 6 3 10 5 16 8 4 2 1



