# pythonic way: use with statement
# no need for file.close

path = 'data.txt'
lines = []
with open(path, 'r') as file:
    lines = file.readlines()

#['hello\n', 'I am\n', 'mostafa\n', '\n', '\n', 'saad ibrahim\n', '12345\n']
print(lines)

