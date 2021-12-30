

path = 'data.txt'
lines = []
with open(path, 'r') as file:
    lines = file.read().splitlines()

# removing the end of line
#['hello', 'I am', 'mostafa', '', '', 'saad ibrahim', '12345']
print(lines)

# you can then do whatever on list
# strip, iterate in reversed way, etc
