
my_list = [1, 'mostafa', 4]

another_list = [99, 11.5]

# 1 mostafa 4 99 11.5
conc_list = my_list + another_list

# 99 11.5 99 11.5
thrd_lst = 2 * another_list

lst = [0] * 6   # 0 0 0 0 0 0

lst += [2, 3] + [5]
# 0 0 0 0 0 0 2 3 5

for item in lst:
    print(item, end=' ')
print()


