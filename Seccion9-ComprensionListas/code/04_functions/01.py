
# .split() return list of strings
my_list = input().split()
for item in my_list:
    print(item, end=' ')
print()

# now list of integers
my_list = list(map(int, input().split()))

print(type(my_list), type(my_list))     # list, int

for item in my_list:
    print(item, end=' ')
print()

# very helpful to read variable number of items on same line
