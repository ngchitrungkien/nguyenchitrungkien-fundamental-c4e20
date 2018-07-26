list_sheep=[5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my sheep sizes")
print(list_sheep,sep=",")
print("Now my biggest sheep has size", max(list_sheep), "let's shear it")
print("After shearing, here is my flock")
x= max(list_sheep)
for n, i in enumerate(list_sheep):
  if i == x:
    list_sheep[n] = 8
print(list_sheep)