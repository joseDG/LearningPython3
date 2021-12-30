
path = 'data.txt'   # relative path (to running point)
file = open(path, 'r')
string = file.readline()

print(string)   # hello

lines = file.readlines()
print(lines)
# ['I am\n', 'mostafa\n', '\n', '\n', 'saad ibrahim\n', '12345\n']

#FileNotFoundError: [Errno 2] No such file or directory: 'notexist.txt'
#open('notexist.txt', 'r')