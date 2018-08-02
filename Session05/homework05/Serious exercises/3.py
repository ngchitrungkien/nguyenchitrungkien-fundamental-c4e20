x= int(input("How many B bacterias are there? "))
y= int(input("How much times in minutes will we wait? "))
bacterias = x * (2 ** (y // 2))

print('After {} minutes, we would have {} bacterias'.format(y,bacterias))