

path = 'output2.txt'

lines = ['Hey', 'Your name?']

# w for write but overwrite
with open(path, 'w') as file:
    for line in lines:
        file.write(line + '\n')





import os
print('*' + os.linesep + '*')