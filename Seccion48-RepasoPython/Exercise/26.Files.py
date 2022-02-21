for number in range(1, 9+1):
    open("day{}.txt".format(number), "w").close()

#version2
for number in range(1, 9+1):
    open("file{}.txt".format(number), "a").close()

#file2.txt
#A leaf is an organ of a vascular plant and is the principal lateral appendage of the stem.

#example3
import glob
import re

text_files = glob.glob("*.txt")
lists =[]
for text_file in text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists, [])

matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
print(sum(numbers)/len(numbers))

"""
file2.txt
capacity11% nodata
capcity33.5% nodata
capacoty3.4% nodata
capacity30% nodata
cap22% nodata
cap34.55%nodata
capacity10%
"""

import glob
import re

text_files = glob.glob("*.txt")
lists =[]
for text_file in text_files:
    with open(text_file) as file:
        lists.append(file.readlines())

all_lines = sum(lists, [])

matches = [re.compile("[0-9]+\.*[0-9]*").search(line) for line in all_lines]

numbers = [float(match.group(0)) for match in matches if match]
mean = sum(numbers)/len(numbers)

with open("mean.txt", "w") as file:
    file.write(str(mean))

#create folders
import os

for i in range(1, 50+1):
    os.makedirs(str(i))

#example5
import os

for folder in range(1, 50+1):
    os.makedirs(str(folder))

for folder in range(1, 50+1):
    for subfolder in ["mon", "tue", "wed", "thu", "fri"]:
        os.makedirs(str(folder) + "/" + str(subfolder))

#delete file
import os
os.remove("file2.txt")

#eleimnar archivos
import glob
import os

text_files = glob.glob("*.txt")
for text_file in text_files:
    os.remove(text_file)


#elimiabr archivos
import glob
import os

text_files = glob.glob("*.txt")

for text_file in text_files:
    with open(text_file) as file:
        content = file.read().lower()
        
    if "xxx" in content:
        os.remove(text_file)

#example 5
import glob
import os

text_files = glob.glob("*.txt")

sizes = {text_file:os.path.getsize(text_file) for text_file in text_files}
print(min(sizes, key=sizes.get))
