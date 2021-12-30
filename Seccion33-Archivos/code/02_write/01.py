path = 'output1.txt'

with open(path, 'w') as file:
    file.write('Hey')
    file.write('Your name?')

# let's run this code twice.
# observe: file will be created if not exist
