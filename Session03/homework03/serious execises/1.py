items=["T-Shirt","Sweater"]
n = str(input("Welcome to our shop, what do you want (C,R,U,D)? "))
if n == str("R"):
    print("Our items: ",end="")
    print(*items,sep=", ")
elif n == str("C"):
    add_item= input("Enter new item: ")
    items.append(add_item)
    print("Our items: ",end="")
    print(*items,sep=", ")
elif n == str("U"):
    items= items + ["Jeans"]
    for item in (items):
        pos = int(input("Update position? "))
        update_item = input("New item? ")
        items[pos - 1] = update_item
        print("Our items: ",end="")
        print(*items,sep=", ")
else:
    delete= int(input("Delete position? "))
    items= items + ["Jeans"]
    items.insert(1,"Skirt")
    items.remove("Sweater")
    items.pop(delete - 1)
    print("Our items: ",end="")
    print(*items,sep=", ")