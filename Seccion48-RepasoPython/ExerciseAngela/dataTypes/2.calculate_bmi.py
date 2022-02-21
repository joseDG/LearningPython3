# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#write your code below this line 👇
weight_as_int = int(weight)
height_as_flaot = float(height)

#using the exponent operator **
bmi = weight_as_int / height_as_flaot ** 2

bmi_as_int = int(bmi)

print(bmi_as_int)
