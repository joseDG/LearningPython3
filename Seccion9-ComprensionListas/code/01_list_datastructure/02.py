
numbers = [10, 2, 7, 5, 3]

numbers[0] = 9
numbers[2] *= 3
numbers[4] += 1

print(numbers[4])


for idx in range(5):
    print(numbers[idx], end=' ')
    # 9 2 21 5 4