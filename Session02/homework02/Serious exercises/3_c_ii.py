x = int(input("Enter a number: "))
i = 1

while i < x+1:
    n = 1
    while n <= x:
        print( "%4d" % (i * n),end="")
        n += 1
    print ("")
    i += 1
print()