list_sheep=[5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my sheep sizes")
print(list_sheep,sep=",")

print("MONTH 1: ")
print("One month has passed, now here is my flock")
plus= [ (i+50) for i in list_sheep]
print(plus)

print("Now my biggest sheep has size", max(plus), "let's shear it")
print("After shearing, here is my flock")
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

print("Now my biggest sheep has size", max(plus2), "let's shear it")
print("After shearing, here is my flock")
x= max(plus2)
for n, i in enumerate(plus2):
  if i == x:
    plus2[n] = 8
print(plus2)
