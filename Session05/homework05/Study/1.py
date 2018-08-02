x = input("Enter a sentence: ").lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

count = {} 
for char in x:
    if char in alphabet: 
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

keys = count.keys()
for char in sorted(keys):
    print(char, count[char])