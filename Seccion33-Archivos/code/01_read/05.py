

path = 'data_utf8.txt'

with open(path, 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()
    print(lines)
    # ['Dürst. ˈmaʳkʊs', '∑∀x∈ℝ H₂ ði ὅ Σὲ ὅτ แผ่']


# UnicodeDecodeError: 'ascii' codec can't decode
# byte 0xc3 in position 1: ordinal not in range(128)
with open(path, 'r', encoding='ASCII') as file:
    lines = file.read().splitlines()
    print(lines)

