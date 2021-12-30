

if __name__ == '__main__':
    n = int(input())
    lst = [0] * n   # more efficient to allocate early

    for pos in range(n):
        name, age, salary = input().split()
        lst[pos] = name, int(age), int(salary)    # tuple

    lst.sort()  # each tuple will be compared
    for idx, (name, age, salary) in enumerate(lst): # deep unpacking
        print(idx, name, age, salary)
