

path, idx = input().split()
idx = int(idx)

file = open(path, 'r')
lst = file.read().splitlines()
print(lst[idx])

file.close()
"""
How many possible exceptions?


data.txt 1          ==> 1
data.txt            ==> ValueError: unpack
not_exist.txt 1     ==> FileNotFoundError
/boot/efi/ 1        ==> PermissionError
data.txt hey        ==> ValueError
data.txt 1000       ==> IndexError
data.txt -1000      ==> IndexError
data.txt -1         ==> 30

"""