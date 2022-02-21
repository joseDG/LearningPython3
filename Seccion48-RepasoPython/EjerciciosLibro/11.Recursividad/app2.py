from operator import length_hint


def length_3n_plus_l(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        return 1 + length_3n_plus_l(n // 2)
    else:
        return + length_3n_plus_l(3*n+1)

print(length_3n_plus_l(6))