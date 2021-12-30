
def read_int(msg):
    try:    # Please execute this code
        age = input(msg)  # 'Hey'
        age = int(age)
    except: # if a crash, run to handle!
        print('Invalid input')
        age = None
    else:   # optional: if no crash, run
        print('Thanks!')
    return age

age = read_int('Enter age: ')
print(age)

"""
Enter age: 10
Thanks!
10
"""