def sq(n):
    return n*n


print(f'__file__ {__file__}')
print(f'__name__ {__name__}')


if __name__ == '__main__':
    # It will never be true if we did not
    # rune ourlib.py ITSELF
    print('Script from ourlib')

