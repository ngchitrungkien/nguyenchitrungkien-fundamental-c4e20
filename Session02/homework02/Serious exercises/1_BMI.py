cm = float(input("Nhap vao chieu cao bang cm cua ban: "))
m = cm/100
print(m)

chieucao = float(input("Nhap vao chieu cao cua ban" + "(don vi: m): "))
cannang = float(input("Nhap vao can nang cua ban"+ "(don vi: kg): "))
BMI = cannang/ (chieucao**2)

if BMI < 16:
    print("Ban can phai giam can!")
elif BMI < 18.5:
    print("Ban dang bi thieu can!")
elif BMI < 25:
    print("Than hinh cua ban hoan toan binh thuong!")
elif BMI < 30:
    print("Ban dang bi thua can!")
else:
    print("Ban bi beo phi roi :(")
