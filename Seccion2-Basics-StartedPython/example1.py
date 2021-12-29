name1 = input("Enter the first student's name: ")
id1 = input("Enter the first student's ID: ")
grade1 = float(input("Enter the first student's grade"))

name2 = input("Enter the second student's name: ")
id2 = input("Enter the second student's ID: ")
grade2 = float(input("Enter the second student's grade"))

print('\n\nInformat for students and their "Math" grades')
msg = name1 + "(ID " + id1 + ")", grade1, str(grade1)
print(msg)
msg = name2 + "(ID " + id2 + ")", grade2, str(grade2)
print(msg)

average = (grade1 + grade2) / 2.0
print("Average math grade is", average)
