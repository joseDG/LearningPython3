n = int(input())

is_even = n % 2 == 0
is_odd = not is_even

# Formula of 2 parts : only one by them will be activates
result = is_even * 100 + is_even * 7

print(result)
