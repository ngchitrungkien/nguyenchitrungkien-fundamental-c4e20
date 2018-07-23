s = 1
def giaithua(n):
    global s
    for i in range (1, n+1):
        s=s*i
    return s

n=int(input("Nhap n: "))

print("{0}! = {1}".format(n, giaithua(n)))
