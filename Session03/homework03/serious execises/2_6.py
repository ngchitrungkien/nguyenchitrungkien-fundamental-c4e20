list_sheep=[5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my sheep sizes")
print(list_sheep,sep=",")
print("Now my biggest sheep has size", max(list_sheep), "let's shear it")
x= max(list_sheep)
for n, i in enumerate(list_sheep):
  if i == x:
    list_sheep[n] = 8
print(list_sheep)

print("MONTH 1: ")
print("One month has passed, now here is my flock")
plus= [ (i+50) for i in list_sheep]
print(plus)
print("Now my biggest sheep has size", max(plus), "let's shear it")
x= max(plus)
for n, i in enumerate(plus):
  if i == x:
    plus[n] = 8
print(plus)

print("MONTH 2: ")
print("One month has passed, now here is my flock")
plus1= [ (i+50) for i in plus]
print(plus1)

print("Now my biggest sheep has size", max(plus1), "let's shear it")
print("After shearing, here is my flock")
x= max(plus1)
for n, i in enumerate(plus1):
  if i == x:
    plus1[n] = 8
print(plus1)

print("MONTH 3: ")
print("One month has passed, now here is my flock")
plus2= [ (i+50) for i in plus1]
print(plus2)

y= sum(plus2)
print("My flock has size in total: " + str(y))
print("I would get "+ str(y) + " * 2$ " + "= " + str(y*2) + "$")