
def our_int(string):
    res = 0
    digits = '0123456789'

    for char in string:
        # search for char in digits to know its value: e.g. convert '5' to 5
        res = res * 10 + digits.find(char)
    return res



if __name__ == '__main__':
    mystr = input()

    ans = our_int(mystr)
    print(ans, ans * 3)

