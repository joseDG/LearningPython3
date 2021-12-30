

path = 'output3.txt'

lines = ['Hey', 'Your name?']

# a for write but append
with open(path, 'a') as file:
    for line in lines:
        file.write(line + '\n')

# let's run this code twice.

