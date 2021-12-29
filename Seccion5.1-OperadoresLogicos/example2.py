num = int(input())


is_even1 = num % 2 == 0


by2 = num / 2.0
by2 = by2 - int(by2)
is_even2 = by2 == 0

last_digit = num % 10
is_even3 = (
    last_digit == 0
    or last_digit == 2
    or last_digit == 4
    or last_digit == 6
    or last_digit == 8
)

print(is_even1, is_even2, is_even3)
