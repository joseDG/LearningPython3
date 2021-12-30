max_num = int(input())

for number in range(2, max_num + 1):
    is_ok = True

    for i in range(2, number):
        if number % i == 0:
            is_ok = False
            break

    if is_ok:
        print(number, end=" ")
