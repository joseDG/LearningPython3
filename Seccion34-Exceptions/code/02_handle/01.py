
def read_int(msg):
    try:
        # Please execute this code
        age = input(msg)  # 'Hey'
        age = int(age)
    except:
        # if a crash, come here to clean!
        print('Invalid input')
        age = None

    return age


age = read_int('Enter age: ')
print(age)

"""
Enter age: aaa
Invalid input
None
"""