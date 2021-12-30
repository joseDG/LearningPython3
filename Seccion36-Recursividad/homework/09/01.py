

def is_prime(m, cur_test_number = 3):
    if m == 2:
        return True

    if m <= 1 or m % 2 == 0:
        return False

    if m == cur_test_number:
        return True

    if m % cur_test_number == 0:
        return False

    return is_prime(m, cur_test_number + 2)


def count_primes(start, end):
    if start > end:
        return 0

    result = is_prime(start)
    result += count_primes(start + 1, end)

    return result


print(count_primes(10, 20))          # 4
print(count_primes(10, 200))         # 42


#print(count_primes(10, 2000))       # RecursionError

