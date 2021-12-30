


path = 'data.txt'
with open(path) as file_reader:
    lst = [abs(int(num)) for num in file_reader]
    print(sum(lst) * max(lst))
