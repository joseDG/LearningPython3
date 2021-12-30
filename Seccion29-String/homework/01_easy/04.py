
# conc strings

def print_conc(str1, str2):
    for c1, c2 in zip(str1, str2):
        print(c1 + c2, end='')

    if len(str1) < len(str2):  # canonicalize: make sure first is bigger
        str1, str2 = str2, str1

    if len(str1) > len(str2):
        print(str1[len(str2):], end='')
    print()

    # observe: I did not explicitly create a new string. Concatenation is slow process
    # always there is a single new line printed not 2 sometimes
    # observe usage of zip
    # observe canonicalization step. Instead of different handling for which is bigger
    # we change content to make sure there is only one case

if __name__ == '__main__':
    str1, str2 = input().split()
    print_conc(str1, str2)


