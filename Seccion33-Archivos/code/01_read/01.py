
path = 'data.txt'   # relative path (to running point)
file = open(path, 'r')  # r is the mode argument for reading

for line in file:   # iterate on files
    # notice, each line has \n in its end
    print(line, end='')

file.close()

"""
Observe printed as lines

hello
I am
mostafa


saad ibrahim
12345
"""