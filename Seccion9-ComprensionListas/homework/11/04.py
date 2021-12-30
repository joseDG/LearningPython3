
def recaman(n):
    if n == 0:
        return 0

    # For N, probably an upper bound value is n * 10
    occurrence = [0] * n * 10   # empty for n = 0
    last_value, occurrence[0] = 0, 1  # first term

    for i in range(1, n+1):
        last_idx = i - 1

        val = last_value - last_idx - 1

        if val < 0 or occurrence[val]:
            val = last_value + last_idx + 1

        occurrence[val], last_value = 1, val

    return last_value

if __name__ == '__main__':
    n = int(input())

    print(recaman(n))
