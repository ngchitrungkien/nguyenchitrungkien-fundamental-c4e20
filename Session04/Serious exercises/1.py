name = input("Your full name: ")
name_low = name.lower()

name_up = name_low.split()
space = " "
print("Updated:  ",end="")
print((space.join(name_up)).title())