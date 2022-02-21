firstname = "John"
lastname = "Smith"

print("Welcome {} {} to our shop!".format(firstname, lastname))


names = {"firstname" : "Andy", "lastname": "Smith"}
print("Welcome {firstname} {lastname} to our shop!".format(**names))


firstname = "Andy"
lastname = "Smith"
print("Welcome {:.1}.{:.1} to our shop!".format(firstname, lastname))
