
input_path = 'input.txt'
output_path = 'output.txt'

with open(input_path, 'r') as reader, \
     open(output_path, 'w') as writer:
    lines = reader.readlines()
    writer.writelines(reversed(lines))
    # writelines doesn't add \n
