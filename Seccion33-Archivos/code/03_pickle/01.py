
lst = [120, 255, 100]

with open("data.binary", "wb") as writer:
    binary_format = bytearray(lst)  # must be in range(0, 256)
    writer.write(binary_format)
    str_encoded = bytearray('abc', 'utf-8')
    writer.write(str_encoded)

with open("data.binary", "rb") as reader:
    lst2 = list(reader.read())
    print(lst2)     # [120, 255, 100, 97, 98, 99]
    # a integer code is 97

