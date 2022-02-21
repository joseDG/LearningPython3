# 🚨 Don't change the code below 👇
print("Welcome to python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L")
add_peperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#Write your code below this line 👇

factura =0 

if size == "S":
    factura += 15
elif size == "M":
    factura += 20
else:
    factura += 25

if add_peperoni == "Y":
    if size == "S":
        factura += 2
    else:
        factura += 3

if extra_cheese == "Y":
  factura += 1
  
print(f"Your final bill is: ${factura}.")