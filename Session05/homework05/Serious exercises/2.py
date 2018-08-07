numbers = ['1', '6', '8', '1', '2', '1', '5', '6']
numb = input("Enter a number? ")
sum= sum(x == numb for x in numbers)
print("{} appears {} in my list".format(numb, sum))
# count = 0
# for n in numbers:
#     if n == numb:
#         count += 1
# print("{} appears {} in my list".format(numb, count))
