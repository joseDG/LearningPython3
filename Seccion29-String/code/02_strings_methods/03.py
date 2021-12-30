
# by default split based on space
print('\n\n\they mostafa'.split())
# ['hey', 'mostafa']

print(' I am   mostafa,saad,ibrahim'.split())
# ['I', 'am', 'mostafa,saad,ibrahim']

print(' I am   mostafa,saad,ibrahim'.split(','))
# [' I am   mostafa', 'saad', 'ibrahim']

print(' I am   mostafa,saad,ibrahim'.split('a'))
#[' I ', 'm   most', 'f', ',s', '', 'd,ibr', 'him']

print('\n\n\they mostafa'.split(' '))
#['\n\n\they', 'mostafa']

print('1,,,2'.split(','))
#['1', '', '', '2']

input().split()

