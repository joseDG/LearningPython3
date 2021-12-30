
def read_int(msg):
    try:
        # Please execute this code
        age = input(msg)  # 'Hey'
        age = int(age)
    except:
        # if a crash, come here to clean!
        print('Invalid input')
        age = None
    finally:    # optional
        # come here regardless crash or not
        print('End of Func')

    return age


age = read_int('Enter age: ')
print(age)

"""
Enter age: aaa
Invalid input
End of Func
None

Enter age: 10
End of Func
10
"""