a, b = map(int, input().split())

is_a_even = a % 2 == 0
is_b_even = b % 2 == 0

if not is_a_even and not is_b_even:
    print(a * b)
elif is_a_even and is_b_even:
    print(a / b)
elif not is_a_even and is_b_even:
    print(a + b)
else:
    print(a - b)
