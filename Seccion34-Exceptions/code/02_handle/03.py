
def read_int(msg):
    try:    # Please execute this code
        age = input(msg)  # 'Hey'
        age = int(age)
    except: # if a crash, run to handle!
        print('Invalid input')
        age = None
    else:   # optional: if no crash, run
        print('Thanks!')
    finally:    # optional: run in all cases
        print('End of Func')

    return age

age = read_int('Enter age: ')
print(age)

"""
Enter age: aaa
Invalid input
End of Func
None

Thanks!
End of Func
20
"""