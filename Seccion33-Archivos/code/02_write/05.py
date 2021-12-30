

path = 'output4.txt'

lines = ['Hey', 'Your name?']

# x: if exist = errio
with open(path, 'x') as file:
    for line in lines:
        file.write(line + '\n')

# let's run this code twice.
# second time error:
# FileExistsError: [Errno 17] File exists:
#   'output4.txt'

